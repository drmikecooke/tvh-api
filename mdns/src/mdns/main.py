from .sender import get
from .tvh import subs,nxt,status
import time

hosts=[b'rpiz1',b'rpiz2',b'rpiz3',b'rpi3a',b'rpi4-128',b'zotac-deb']
pad='\n'+' '*12

def timeform(t):return time.strftime("%a, %d %b %Y %H:%M", time.localtime(t))

def warn(message):return f"\x1b[91;1m{message}\x1b[0m"

def main():
    for host in hosts:
        data,server=get(host)
        string=f'\n{host.decode("ascii"):>10s}:'
        if server:
            ip=server[0]
            output=[]
            try:
                states=subs(ip)
                if states:
                    output+=[', '.join(states)]
                nxtprg=nxt(ip)
                if nxtprg:
                    if nxtprg>time.time():
                        output+=['next recording at '+timeform(nxtprg)]
                    if nxtprg-time.time()>1800:
                        alarm=timeform(nxtprg-1800) # half hour
                        output+=[warn(f'set alarm for {alarm}')]
                else:
                    output+=['no recordings scheduled']
                result=status(ip)
                errors={key: result[key] for key in result if result[key]}
                if errors:
                    output+=[warn(f'errors {errors}')]
            except:
                output+=['no tvh connection']
            print(string,pad.join(output))
        else:
            print(string,'no ip connection')
    print()
