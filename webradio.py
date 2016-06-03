#!/usr/bin/python
import os
#import thread
import ConfigParser
from time import sleep

def threadWebradioService(sPathToConfig = '/var/sensorTool/www/webradio.station'):
    config = ConfigParser.RawConfigParser()
    config.read(sPathToConfig)
    
    if config.getboolean('running', 'changed'):
        sArg = config.get('running',  'action') + ' ' + config.get('running',  'stream')+' '+config.get('running',  'volume')
        #print sArg
        os.system("/home/pi/webradio/webradio.sh " + sArg +" &")
        #os.system("echo \""+sArg+"\"")
        config.set('running', 'changed', False)
        with open(str(sPathToConfig), 'wb') as configfile:
            config.write(configfile) 
   
def threadwebradiotest():
    while True:
        #print 'thread'
        threadWebradioService()
        sleep(5)

threadwebradiotest()    
