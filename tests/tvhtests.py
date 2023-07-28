import sys
sys.path.append('../src')
from tvhAPI_pkg.api import setUSR,subs,inputs,nxt
from socket import gethostbyname

def getIP4(url):
    return gethostbyname(url)
    
setUSR()
tvh=input("tvh: ")
print(getIP4(tvh+".local"))
print(subs(tvh))
print(inputs(tvh))
print(nxt(tvh))
