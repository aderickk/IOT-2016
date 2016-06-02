#!/bin/sh
while true; do
    INPUT=$(mosquitto_sub -t "groupD/Temperature" -C 1)
    #echo $INPUT
    mosquitto_sub -d -t "groupD/Temperature" | tee -a mqtt_log.csv | sed '$!d'  
sleep 1   
done 
