#!/bin/sh
###
# init service for the kbd-backlight service
###

DAEMON='/usr/local/bin/kbd-backlight.py'
PID_FILE='/var/run/kbd-backlight.pid'

case $1 in
        start)
		/sbin/start-stop-daemon -v -p PID_FILE -m -b --exec $DAEMON --start
		;;
        stop)
		/sbin/start-stop-daemon -v -p /var/run/kbd-backlight.pid --remove-pid --stop
		;;
        restart|force-reload)
                $0 stop && sleep 2 && $0 start
                ;;
	status)
		echo 'not implemented'
		;;
        *)
                echo "Usage: $0 {start|stop|restart|try-restart|force-reload|status}"
                exit 2
                ;;
esac

