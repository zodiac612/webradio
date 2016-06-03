#!/bin/bash
# 
#echo "$1" > /home/pi/sensorTool/sh/tempbase.txt

vBase64=$1
python /home/pi/webradio/updatewebradio.py $vBase64
#vPARAMS=$(echo "$1" | base64 -d)
#echo $vPARAMS
#/home/pi/webradio/webradio.sh $vPARAMS

