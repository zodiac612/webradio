# Readme.txt
# How To enable commandline Audio to RPI

# Configure Raspberry PI
sudo raspi-config
# 8 Advanced Options
# A9 Audio
# 1 Force 3.5mm ('headphone') jack
# If you get an error running option A9 Audio
#  then activate audio via
sudo vi /boot/config.txt
# and add the line (I add it after the last dtparam entry)
# dtparam=audio=on
# and reboot
# When a 3.5mm speaker is connected at start than "0 Auto" also works fine
# HDMI is not connected in my configuration 

# Install mplayer
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mplayer

# To start a stream start mplayer with the correct URL e.g.
mplayer http://stream.radio8.de:8000/live
# mplayer should start, load, playing the stream.
# If not then you probably do not have the right URL
# from the radio8.de website i got the url:
# mplayer http://stream.radio8.de:8000/live.m3u
# But mplayer only exits: Exiting... (End of file)
# So i downloaded the live.m3u file and used the url out of the file

# While streaming and playing the stream on my wavemaster mobil box
# the rpi only needs 0,07W more and mplayer only uses about 5% CPU

webradio.php
## php file integration for sensorTool
## via POST methode the parameter are convertatd with base64
## base64-value is passed to shell skript
updatewebradio.sh
## which starts the python update skript
updatewebradio.py
## converts base 64 back to dictonary and saves the config file
webradio.station

webradio.py
## webradio.py reads config file and starts or stops the webradio stream using
webradio.sh
## which starts mplayer and sets the volume.
