# -*- coding: UTF-8 -*-

#!/usr/bin/python
# 
# Filename:  UDP_connections.py 
#
# Version: 1.0.1
#
# 
# ================================================================================================
#
# Función:  UDP_connections()
#
# Descripción:   Módulo que permite realizar conecciones por el protocolo UDP
#                (User Datagram Protocol)
#
#
# Parámetros: Recibe como parámetro una dirección IP o un segmento completo:
# 
#
# Ejemplo: 192.168.1.5 o también 192.168.1.0/24 
# 
# 
# ================================================================================================
from colorama import init, Fore, Back, Style
import os, sys, datetime, time, random, importlib,ftplib, urllib
import socket




def requests(direccion_IP):
    cont=0
    while(cont<10000):
        #print("Peticiones por UDP")
        mensaje=""
        sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(mensaje), (direccion_IP, 22))
        sock.sendto(bytes(mensaje), (direccion_IP, 21))
        sock.sendto(bytes(mensaje), (direccion_IP, 23))
        sock.sendto(bytes(mensaje), (direccion_IP, 53))
        sock.sendto(bytes(mensaje), (direccion_IP, 80))
        sock.sendto(bytes(mensaje), (direccion_IP, 443))
        sock.sendto(bytes(mensaje), (direccion_IP, 445))
        sock.sendto(bytes(mensaje), (direccion_IP, 1533))
        sock.sendto(bytes(mensaje), (direccion_IP, 3389))
        sock.sendto(bytes(mensaje), (direccion_IP, 5900))

        cont=cont+1

        
