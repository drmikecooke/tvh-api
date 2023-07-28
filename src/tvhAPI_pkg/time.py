import time

def midnight(day):
	m=list(time.localtime(time.time()+day*24*3600))+['GMT']
	m[3:6]=[0,0,0]
	return int(time.mktime(time.struct_time(m)))

def midnights(days):
	return [midnight(day) for day in days]

def tmfmt(fmt,et):
	return time.strftime(fmt, time.localtime(et))
	
def wndw(day,hstart,hstop):
	m=midnight(day)
	return [m+hstart*3600,m+hstop*3600]

