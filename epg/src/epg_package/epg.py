# ideas from:

# https://github.com/Finn10111/tvh-auto-power/blob/master/tvh-auto-power.py

# https://github.com/dave-p/TVH-API-docs/wiki/

from .api import getAPI

def getEPG(tvh,channel):
    data=getAPI(tvh,f'epg/events/grid?channel={channel}&limit=1000')
    if 'entries' in data.keys():
        return data['entries']

def checkEPG(epg): # is EPG full?
    for i in range(len(epg)-1):
        if epg[i]['stop']!=epg[i+1]['start']:
            print('Damn')

