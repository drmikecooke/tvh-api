from .api import setUSR,subs,inputs,nxt
import sys
import time
from socket import gethostbyname,gaierror

def timeform(t):return time.strftime("%a, %d %b %Y %H:%M", time.localtime(t))

def warn(message):print(f"\x1b[91;1m{message}\x1b[0m")

def main():
    from sys import argv
    setUSR()
    tvh="rpi"+argv[1] if len(argv)>1 else "rpi"+input("tvh: ")
    try:
        print("Host: ",tvh,"@ IPv4:",gethostbyname(tvh+".local"))
    except gaierror:
        print("Host: ",tvh,"not responding")
        sys.exit(1)
    for item in subs(tvh):
        warn(' '*12+item)
    errs=inputs(tvh)
    print(' '*12+errs["input"])
    del errs["input"]
    nzerrs={key:errs[key] for key in errs if errs[key]>0}
    if nzerrs:
        warn(' '*12+str(nzerrs))
    start,stop=nxt(tvh)
    if not start:
        print(' '*12+'No recordings scheduled')
        sys.exit(0)
    if start<time.time():
        print(' '*12+f'first stop at {timeform(stop)}')
    else:
        print(' '*12+f'next start at {timeform(start)}')
        if start-time.time()>1800:
            alarm=timeform(start-1800) # half hour prep
            warn(' '*12+f'set alarm for {alarm}')
