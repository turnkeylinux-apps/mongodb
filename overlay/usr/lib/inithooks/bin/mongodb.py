#!/usr/bin/python
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
from executil import ExecError, system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass='])
    except getopt.GetoptError, e:
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

    escaped_pass = re.escape(new_pass)
    script = os.path.dirname(__file__)+'/mongodb.sh'
    system(script, escaped_pass)
    print "Set new password for admin user."


if __name__ == "__main__":
    main()

