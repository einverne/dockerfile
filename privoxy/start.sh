#!/bin/sh

CONFFILE=/etc/privoxy/config
PIDFILE=/var/run/privoxy.pid

if [ ! -f "${CONFFILE}" ]; then
	echo "Configuration file ${CONFFILE} not found!"
	exit 1
fi

/usr/sbin/privoxy --no-daemon --pidfile "${PIDFILE}" "${CONFFILE}"
