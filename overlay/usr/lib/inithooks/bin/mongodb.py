#!/usr/bin/python3
"""Set MongoDB admin password

Option:
    --pass=            unless provided, will ask interactively

"""

import sys
import time
import getopt
import re
import os

from dialog_wrapper import Dialog
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

    script = os.path.join(os.path.dirname(__file__), 'mongodb.sh')
    subprocess.run([script, new_pass])
    print("Set new password for admin user.")


if __name__ == "__main__":
    main()

