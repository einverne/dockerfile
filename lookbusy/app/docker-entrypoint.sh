#!/bin/bash
set -e

# speedtest
if [ $SPEEDTEST_INTERVAL ]; then
    # create crontab
    if [ $SPEEDTEST_INTERVAL -eq 0 ]; then
        echo "Interval is 0, no task will be created"
    elif [ $SPEEDTEST_INTERVAL -le 59 ]; then
        echo -e "*/${SPEEDTEST_INTERVAL}\t*\t*\t*\t*\tnohup bash /app/speedtest.sh >/app/speedtest.log 2>&1 &" | crontab
        echo "Scheduled task created successfully"
        service cron restart
    elif [[ $SPEEDTEST_INTERVAL -gt 59 && $SPEEDTEST_INTERVAL -lt 1440 ]]; then
        hour=$(($SPEEDTEST_INTERVAL / 60))
        minute=$(($SPEEDTEST_INTERVAL % 60))
        echo -e "$minute\t*/$hour\t*\t*\t*\tnohup bash /app/speedtest.sh >/app/speedtest.log 2>&1 &" | crontab
        echo "Scheduled task created successfully"
        service cron restart
    else
        echo "Interval limit exceeded"
    fi

else
    echo "SPEEDTEST_INTERVAL is not exists"
fi

# lookbusy
MemTotal=$(awk '($1 == "MemTotal:"){printf "%d\n",$2/1024}' /proc/meminfo) # total memory
if [ $CPU_CORE ]; then
    if [ $MEM_UTIL ]; then
        MemUsage=$(($MemTotal / 100 * $MEM_UTIL))
        lookbusy -c $CPU_UTIL -n $CPU_CORE -m ${MemUsage}MB
    else
        lookbusy -c $CPU_UTIL -n $CPU_CORE
    fi
else
    if [ $MEM_UTIL ]; then
        MemUsage=$(($MemTotal / 100 * $MEM_UTIL))
        lookbusy -c $CPU_UTIL -r curve -m ${MemUsage}MB
    else
        lookbusy -c $CPU_UTIL -r curve
    fi
fi
