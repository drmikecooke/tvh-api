# ideas from:

# https://github.com/Finn10111/tvh-auto-power/blob/master/tvh-auto-power.py

# https://github.com/dave-p/TVH-API-docs/wiki/

import requests
from requests.auth import HTTPDigestAuth
import time
from json import loads

def getAPI(tvh,api):
    bUrl=f'http://{tvh}.local:9981/api/'
    try:
        response=requests.get(bUrl+api,auth=HTTPDigestAuth(USER,PWD))
    except requests.ConnectionError:
        return {'help':0} # indicate not connected
    return loads(response.text,strict=False)
