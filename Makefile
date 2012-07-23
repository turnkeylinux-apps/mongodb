root.build/ignore-errors = mongodb-server mongodb-dev mongodb

WEBMIN_FW_TCP_INCOMING = 22 80 443 12320 12321 27017 27018 27019 28017

COMMON_CONF = lighttpd-fastcgi

include $(FAB_PATH)/common/mk/turnkey/php.mk
include $(FAB_PATH)/common/mk/turnkey.mk
