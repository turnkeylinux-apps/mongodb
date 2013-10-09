#!/usr/bin/python
"""Set MongoDB admin password

Option:
    --pass=            unless provided, will ask interactively
    --current-pass=    unless provided, will ask interactively

"""

import sys
import time
import getopt
import pymongo

from dialog_wrapper import Dialog
from executil import ExecError, system

class MongoDBError(Exception):
    pass

class MongoDB:
    def __init__(self, dbname="admin", username="admin", cur_pass=""):
        self.dbname = dbname
        self.username = username

        self.selfstarted = False
        if not self._is_alive():
            self._start()
            self.selfstarted = True

        self.conn = self._connect()
        self.db = self.conn[dbname]

        if cur_pass:
            auth = self.db.authenticate(self.username, cur_pass)
            if not auth:
                raise MongoDBError("Authentication failed for %s account" % username)

    @staticmethod
    def _connect(max_attempts=20, sleep=3):
        attempt = 0
        while True:
            attempt += 1
            try:
                conn = pymongo.Connection()
                return conn
            except:
                time.sleep(sleep)
                if attempt >= max_attempts:
                    raise MongoDBError("Exhausted connection attempts")

    def _is_alive(self):
        try:
            system("/etc/init.d/mongodb status")
        except ExecError, e:
            return False

        return True

    def _start(self):
        system("/etc/init.d/mongodb start")

    def _stop(self):
        if self.selfstarted:
            system("/etc/init.d/mongodb stop")

    def __del__(self):
        self._stop()

    def setpass(self, new_pass):
        self.db.add_user(self.username, new_pass)

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'current-pass='])
    except getopt.GetoptError, e:
        usage(e)

    new_pass = ""
    cur_pass = None

    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            new_pass = val
        elif opt == '--current-pass':
            cur_pass = val

    if cur_pass == None:
        d = Dialog('TurnKey Linux - First boot configuration')
        cur_pass = d.get_password(
            "MongoDB current password",
            "Enter current password for the MongoDB 'admin' account.")

    if not new_pass:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        new_pass = d.get_password(
            "MongoDB Password",
            "Enter new password for the MongoDB 'admin' account.")

    if cur_pass == new_pass:
        print "current and new passwords do not differ, exiting..."
        return

    mongodb = MongoDB(username="admin", cur_pass=cur_pass)
    mongodb.setpass(new_pass)
    print "Set new password for admin user."


if __name__ == "__main__":
    main()

