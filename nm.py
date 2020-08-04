#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nm.py
#  
#  Copyright 2019 Julio <julio@julio-HP-Compaq-Pro-6305-SFF>
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


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import nmap
    nm = nmap.PortScanner()
    IP='192.168.0.5'
    nm.scan(IP, '22-443')
    for host in nm.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, nm[host].hostname()))
     print('State : %s' % nm[host].state())
     for proto in nm[host].all_protocols(): 
         print('----------')
         print('Protocol : %s' % proto)
         lport = nm[host][proto].keys()
         lport.sort()
         for port in lport:
			 print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
    
