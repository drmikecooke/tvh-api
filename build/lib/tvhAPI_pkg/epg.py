# ideas from:

# https://github.com/Finn10111/tvh-auto-power/blob/master/tvh-auto-power.py

# https://github.com/dave-p/TVH-API-docs/wiki/

from .page import page
from .api import setUSR
from pathlib import Path
from .channels import chlist

def main():
    from sys import argv
    setUSR()
    tvh="rpi"+argv[1] if len(argv)>1 else "rpi"+input("tvh: ")        
    print("Host",tvh)

    day=int(argv[2]) if len(argv)>2 else 1	
    
    times=[2,10,18,26]
    if len(argv)>3:
        times=[int(number) for number in argv[3:]]
    
    chf=Path.home()/".epg.conf"
    if chf.is_file():
        with open(chf,"rt") as chsf:
            channels=chsf.read().split("\n")[:-1]
    else:
        print("Getting fresh channel list")
        channels=chlist(tvh)
        print("Saving list at:",chf)
        with open(chf,"wt") as chsf:
            chsf.write('\n'.join(channels))
            
    start=times[0]
    for stop in times[1:]:
        page(day,start,stop,tvh,channels)
        start=stop        
    return 0
