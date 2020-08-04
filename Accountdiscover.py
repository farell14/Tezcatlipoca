# -*- coding: UTF-8 -*-

#!/usr/bin/python
# 
# Filename:  AccountDiscover.py 
#
# Version: 1.0.1
# 
# 
# 
# ================================================================================================
from colorama import init, Fore, Back, Style
import os,sys, telnetlib, ftplib
import NetworkScanning
import sys
import nmap


def ReadFile():
    print("Lectura de archivos...")
    file = open("Diccionario.conf", "r")
    print(file.read())
    file.close()


def WriteFile():
    print("Escritura de datos...")
    file=open("Resultados.conf", "w")
    ####
    file.close()



def FTPDiscover(Direccion_IP):
    print("Servicio FPT")
    ip=Direccion_IP
    orden="nmap --script ftp-brute -p 21"
    os.system(orden+ip)
    nm = nmap.PortScanner()
    nm.scan(ip,'21')
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
    return ip
    

def TelnetDiscover(Direccion_IP):
    print("Accesos por defecto en Telnet")
    #conn=telnetlib.Telnet(Direccion_IP)
    orden="nmap -p 23 --script telnet-ntlm-info"
    ip=Direccion_IP
    os.system(orden+ip)
    nm = nmap.PortScanner()
    nm.scan(ip,'21')
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
    return ip

def SMBDiscover(Direccion_IP):
    nm = nmap.PortScanner()
    print("Enumeración SMB")
    nm.scan(Direccion_IP,'139-445')
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
    


    