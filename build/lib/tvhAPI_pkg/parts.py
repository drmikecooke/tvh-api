from .html import div,flex,wrap
from .blks import chblk,style
from .time import tmfmt
import time

def scale(hstart,hstop):
    timeBlocks=[chblk('')]
    timeBlocks+=[div(style(200,'lightblue'),f'{t%24}') for t in range(hstart,hstop)]
    return flex(''.join(timeBlocks))

def centered(content):
    stl='width:1725px;position:relative;margin:auto;margin-bottom:100px'
    return div(stl,content)

def name(day,hstart,hstop):
    return f"EPG{tmfmt('%y%m%d', day)},{hstart*100:04d}-{hstop%24*100:04d}"
    
def title(day,hstart,hstop):
	return wrap('title','',name(day,hstart,hstop))

def heading(t):
    return wrap("h1",'style="text-align:center;"',f'EPG: {tmfmt("%a, %d %b %Y", t)}')+"<br/>"
