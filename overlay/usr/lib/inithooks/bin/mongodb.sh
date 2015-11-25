#!/bin/bash -e

[ -n "$1" ]

/etc/init.d/mongodb stop
echo "starting mongod with '--noauth'; logging to syslog"
mongod --dbpath /var/lib/mongodb --noauth --fork --syslog --quiet --bind_ip 127.0.0.1
echo "resetting 'admin' password"
mongo admin --eval "db.changeUserPassword(\"admin\",\"$1\");" --quiet
echo "killing mongod process and restarting service"
mongod --dbpath /var/lib/mongodb --shutdown --quiet
/etc/init.d/mongodb start

