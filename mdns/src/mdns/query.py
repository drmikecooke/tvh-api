from struct import pack

QTYPE={'A':pack('>H',1),'AAAA':pack('>H',28),'PTR':pack('>H',12)}

def NAME(bytestr):return pack(f"{len(bytestr)+1}p",bytestr)

domain=b'local'
DOMAIN=NAME(domain)

def QUERY(HOST,typestr="A"):
    QNAME=NAME(HOST)+DOMAIN+b"\x00" # 0 termination
    QCLASS=pack('>H',1|1<<15) # set unicast response
    return QNAME+QTYPE[typestr]+QCLASS
    
def PACKET(HOST):
    HEADER=pack('>HH',0,0) # ID and flags
    RECORDS=pack('>HHHH',1,0,0,0) # questions,anss,auth,add
    return HEADER+RECORDS+QUERY(HOST)
