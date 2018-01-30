#!/bin/bash -e

[ -n "$1" ]

service mongodb stop
echo "starting mongod with '--noauth'; logging to syslog"
su -c 'mongod --dbpath /var/lib/mongodb --noauth --fork --syslog --quiet --bind_ip 127.0.0.1' -s /bin/bash mongodb
echo "resetting 'admin' password"
mongo admin --eval "db.changeUserPassword(\"admin\",\"$1\");" --quiet
echo "killing mongod process and restarting service"
mongod --dbpath /var/lib/mongodb --shutdown --quiet
service mongodb start

