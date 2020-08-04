# -*- coding: UTF-8 -*-

#!/usr/bin/python
# 
# Filename:  NetworkScanning.py 
#
# Version: 1.0.1
#
# 
# ================================================================================================
#
# Función:  NetworkScanning()
#
# Descripción:   Función que permite seleccionar las diferentes herramientas de escaneo de  
# puertos basados en consola, Nmap, Nikto y Masscan.
#
# Nmap: Escaneo en busca de puertos relacionados a gestored de bases de datos abiertos "1433
#       1521, 3306, 27017,27018, 27019, 28017, 5000, 5001.
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



def PortDiscover(direccion_IP):
    cadena=""
    print("Analizando dirección : ")
    print(direccion_IP)
    orden="nmap -Pn -n --open -sT -sV -p1433,1521,3306,27017,27018,27019,28017,5000,5001 "
    print("Escaneando con:" +orden)
    os.system(orden+direccion_IP)
    orden="nmap -Pn -n --open -sT -sV -p3389,5900 "
    print("Escaneando con:" +orden)
    os.system(orden+direccion_IP)
    orden="nmap -Pn -n --open -sT -sV -p21,22,23"
    os.system(orden+direccion_IP)

def top1000(direccion_IP):
    print("Primeros 1000 puertos ")
    orden="nmap -Pn -n --open -sT -sC"
    print("Escaneando con:"+orden)
    os.system(orden+direccion_IP)

def SMBScann(direccion_IP):
    print("SMB Service")
    orden="nmap -Pn -n --open -sT -sV -p139,445 --script=smb-os-discovery,smb-system-info,smb-enum-users,smb-enum-shares"
    print("Escaneando con :"+orden)
    os.system(orden+direccion_IP)





def VulnsScan(direccion_IP):
    cadena=""
    print("Ejecutando análisis de vulnerabilidades \n")
    orden="nikto -h "
    IP1=direccion_IP
    os.system(orden+IP1)
    
