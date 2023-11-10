# ideas from:

# https://github.com/Finn10111/tvh-auto-power/blob/master/tvh-auto-power.py

# https://github.com/dave-p/TVH-API-docs/wiki/

import requests
from requests.auth import HTTPDigestAuth
import time
from json import loads
from os import environ

statkeys=["input","ber","ec_bit","ec_block","tc_bit","tc_block","te","cc","unc"]

def getAPI(tvh,api):
    bUrl=f'http://{tvh}.local:9981/api/'
    try:
        response=requests.get(bUrl+api,auth=HTTPDigestAuth(__USER__,__PWD__))
    except requests.ConnectionError:
        return {'help':0} # indicate not connected
    return loads(response.text,strict=False)

def setUSR():
    global __USER__,__PWD__
    if "TVH" in environ:
        __USER__,__PWD__=environ["TVH"].split(":")
    else:
        __USER__,__PWD__=input("user: "),input("pwd: ")
    
def subs(tvh):
    hd=getAPI(tvh,"status/subscriptions")
    return [entry['title'] for entry in hd['entries']]
    
def inputs(tvh):
    sd=getAPI(tvh,'status/inputs')['entries'][0]
    return {key:sd[key] for key in statkeys}

def nxt(tvh):
    gd=getAPI(tvh,"dvr/entry/grid_upcoming")
    if gd['total']>40:
        print(f'Check all entries for {tvh}\n')
    starts=[item['start_real'] for item in gd['entries']]
    stops=[item['stop_real'] for item in gd['entries']]
    if starts:
        return min(starts),min(stops)
    return None,None
