#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hello.py
#  
#  Copyright 2023  <mike@rpi3-32>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from .epg import getEPG
from .page import page
from pathlib import Path
from .channels import chlist

def main():
    from sys import argv
    
    tvh="rpiz3"
    if len(argv)>1:
        tvh="rpi"+argv[1]
    print("Host",tvh)

    day=1	
    if len(argv)>2:
        day=int(argv[2])
    
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
