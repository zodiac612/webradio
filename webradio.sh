#!/bin/bash

SCRIPT1="mplayer"

PID=`ps -ef | grep $SCRIPT1 | awk '$0!~/grep/ && $2~/[0-9]/{print $2}'`;

case "$1" in 
    start)
        if [ -z $2 ] 
        then 
            vSTREAM="http://stream.radio8.de:8000/live"
        else
            vSTREAM=$2
        fi
        
        if [ ! -z "$PID" ] ; then
            killall $SCRIPT1 >/dev/null 2>&1
            echo "running webradio already running => stopped"
        fi
            echo "Starting webradio with Stream :" $vSTREAM
            $SCRIPT1 $vSTREAM   >/dev/null 2>&1 &
        ;;     
    status)
        if [ -z "$PID" ] ; then
            echo "webradio not started yet"
        else
            echo "webradio is running:" $PID
        fi
        ;;
    stop)
        if [ -z "$PID" ] ; then
            echo "webradio not started"
        else
            echo "Stopping mplayer" $PID
            killall $SCRIPT1 >/dev/null 2>&1
        fi
        ;;
    *)
        echo "USAGE webradio start [stream] | stop | status"
        exit 1
        ;;
esac
exit 0
