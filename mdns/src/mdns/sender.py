from struct import pack
import socket as sock
from .query import PACKET

def get(HOST):
    multicast_group = ("224.0.0.251", 5353)
    sender=sock.socket(sock.AF_INET,sock.SOCK_DGRAM)
    sender.settimeout(1)
    ttl = b'\x01'
    sender.setsockopt(sock.IPPROTO_IP,sock.IP_MULTICAST_TTL, ttl)
    sent = sender.sendto(PACKET(HOST), multicast_group)

    try:
        data, server = sender.recvfrom(4096)
    except sock.timeout:
        data,server=None,None
    sender.close()
    return data, server
