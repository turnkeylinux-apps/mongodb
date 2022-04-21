#!/usr/bin/python3
"""Set MongoDB admin password

Option:
    --pass=            unless provided, will ask interactively
    --ui_pass=         unless provided, will ask interactively

"""

import sys
import time
import getopt
import re
import os
import json

from libinithooks.dialog_wrapper import Dialog
from libinithooks import inithooks_cache
import subprocess

def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass='])
    except getopt.GetoptError as e:
        usage(e)

    new_pass = ""
    ui_pass = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            new_pass = val

    if not new_pass:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        new_pass = d.get_password(
            "MongoDB Password",
            "Enter new password for the MongoDB 'admin' account.")

    if not ui_pass:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        ui_pass = d.get_password(
            "Mongo-Express UI Password",
            "Enter new password for the MongoDB GUI Control Panel 'admin' account.")


    JSON="/opt/tklweb-cp/ecosystem.config.js"


    subprocess.run(['sed', '-i', 's|\"ME_CONFIG_BASICAUTH_PASSWORD\": \".*\"|\"ME_CONFIG_BASICAUTH_PASSWORD\": \"%s\"|'  % ui_pass, "/opt/tklweb-cp/ecosystem.config.js"])


    script = os.path.join(os.path.dirname(__file__), 'mongodb.sh')
    subprocess.run([script, new_pass])
    print("Set new password for admin user.")

    # reload and restart pm2 so changes take affect
    # and save them to /home/node/.pm2/dump.pm2
    try:
        subprocess.run(["systemctl", "is-active",
                        "--quiet", "pm2-node.service"])
        subprocess.run(["systemctl", "daemon-reload"])
        subprocess.run(["pm2", "reload", "/opt/tklweb-cp/ecosystem.config.js"],env={"PM2_HOME": "/home/node/.pm2", "PATH": "/usr/local/bin"}, check=True, user="node")
        subprocess.run(["pm2", "save"],env={"PM2_HOME": "/home/node/.pm2", "PATH": "/usr/local/bin"}, check=True, user="node")
        subprocess.run(["service", "pm2-node", "restart"])
    except ExecError:
        pass

if __name__ == "__main__":
    main()

