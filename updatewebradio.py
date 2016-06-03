#!/usr/bin/python
import ConfigParser, sys, ast
import base64
import hashlib

sPathToConfig = '/var/sensorTool/www/webradio.station'
config = ConfigParser.RawConfigParser()
config.read(sPathToConfig)

dictResponse = ast.literal_eval(str(base64.b64decode(sys.argv[1])))
vSave = False
vStop = False

#for vName in dictResponse:
vSection = 'running'
 #   vValue= dictResponse[vName]

#vParams = ''
if 'action' in dictResponse:
    if config.get(vSection, 'action') <> dictResponse['action']:
        if dictResponse['action'] == 'start':
            config.set(vSection, 'action', dictResponse['action'])
            #vParams = 'start'
            vSave = True
        else:
            config.set(vSection, 'action', dictResponse['action'])
            #vParams = 'stop'
            vSave = True
            vStop = True

if 'stream' in dictResponse:            
    if not vStop and config.get(vSection, 'stream') <> dictResponse['stream']:
        config.set(vSection, 'stream', dictResponse['stream'])
        #vParams += ' '+str(dictResponse['stream'])
        vSave = True

if 'volume' in dictResponse:        
    if not vStop and config.get(vSection, 'volume') <> dictResponse['volume']:
        config.set(vSection, 'volume', dictResponse['volume'])
        #vParams += ' -af volume='+str(dictResponse['volume'])
        vSave = True

if vSave:
    config.set(vSection, 'changed', True)
    with open(str(sPathToConfig), 'wb') as configfile:
        config.write(configfile) 
