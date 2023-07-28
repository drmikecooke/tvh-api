from .html import head,body,html,flex
from .parts import centered,scale,title,heading,name
from .time import midnight,wndw
from .blks import chblk,blk
from .api import getAPI

def getEPG(tvh,channel):
    data=getAPI(tvh,f'epg/events/grid?channel={channel}&limit=1000')
    if 'entries' in data.keys():
        return data['entries']

def checkEPG(epg): # is EPG full?
    for i in range(len(epg)-1):
        if epg[i]['stop']!=epg[i+1]['start']:
            print('Damn')

def page(day,hstart,hstop,tvh,channels):
	now=midnight(0)
	d=now+day*24*3600 # seconds from epoch
	start,stop=wndw(day,hstart,hstop)
	scl=scale(hstart,hstop)
	content=heading(d)
	for ch in channels:
		epgch=getEPG(tvh,ch)
		content+=scl
		row=chblk(ch)
		for i in range(len(epgch)-1):
			if epgch[i]['start']>=stop:
				break
			if epgch[i]['stop']!=epgch[i+1]['start']:
				'''check for gap'''
				#print("Gap after:",epgch[i])
			if start < epgch[i]['stop']:
				dt=min(epgch[i]['stop'],stop)-max(epgch[i]['start'],start)
				row+=blk(epgch[i],dt)
		content+=flex(row)				
	pg=html(head(title(d,hstart,hstop)),body(content+"<br/>"))
	print("Making:",name(d,hstart,hstop))
	print(pg,file=open(name(d,hstart,hstop)+".html","w"))
