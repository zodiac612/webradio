#!/usr/bin/python
import os
#import thread
import ConfigParser
from time import sleep

def threadWebradioService(sPathToConfig = '/var/sensorTool/www/webradio.station'):
    configRadio = ConfigParser.RawConfigParser()
    configRadio.read(sPathToConfig)
    
    if configRadio.getboolean('running', 'changed'):
        sArg = configRadio.get('running',  'action') + ' ' + configRadio.get('running',  'stream')+' '+configRadio.get('running',  'volume')
        #print sArg
        os.system("/home/pi/webradio/webradio.sh " + sArg +" &")
        #os.system("echo \""+sArg+"\"")
        configRadio.set('running', 'changed', False)
        with open(str(sPathToConfig), 'wb') as configRadioFile:
            configRadio.write(configRadioFile) 
   
def threadwebradiotest():
    while True:
        #print 'thread'
        threadWebradioService()
        sleep(5)

threadwebradiotest()    
