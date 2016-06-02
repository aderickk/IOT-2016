#!/bin/sh
while true; do
    echo $(vcgencmd measure_temp)
    sleep 1
done | mosquitto_pub -l -t "groupD/Temperature"
