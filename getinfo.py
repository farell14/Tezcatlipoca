# -*- coding: UTF-8 -*-

#!/usr/bin/python
# 
# Filename:  get-info.py 
#
# Version: 0.0.1
#
# 
# ================================================================================================
#
# Función:  GetInfo()
#
# Descripción:   Función que permite obtener información del equipo para la realización del
#                análisis automatizado, entre sus funciones está el obtener la dirección IP 
#                del equipo desde el cuál se está ejecutando el script, la puerta de enlace                
#                predeterminada y el segmento en el cuál se encuentra.
#               
#
#               Devuelve los siguientes parámetros:
#
#
# 
# Parámetros:   Dirección IP del equipo
#               Puerta de enlace predeterminada (gateway)   
#               Segmento de red en el que se encuentra ubicado
#               Información de la interfaz física
# 
# 
# 
# 
# ================================================================================================
from colorama import init, Fore, Back, Style
import os, sys, datetime, time, random, importlib,ftplib, urllib
import socket

def menu():
    print("Bienvenido al asistente de confiuguración del entorno: \n \n")
    print("Por favor, selecciona el modo de operación: \n \n")
    print("1. Manual")
    print("2. Automático")
    print (Fore.BLUE+"\n     Ingresa una opción")
    seleccionInvalida=1
    while (seleccionInvalida):
            try:
                op=input(Fore.WHITE+'~ $ ')
                if(op> 0 and op <3):
                    seleccionInvalida=0
                else:
                    print("Seleccion inválida, Intenta nuevamente")
            except ValueError:
                print("Seleccion inválida, Intenta nuevamente")
    return op

def automatico():
    print("Configuración automática...\n \n")
    print("Obteniendo información...\n \n")
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print(hostname)    
    #print(IPAddr) 
    net=IPAddr
    net=IPAddr+"/24"
    return net
    



def manual():
    print("Configuración manual...\n \n")
    IP=raw_input("Ingresa la dirección o segmento de Red a analizar:_")
    net=IP+"/24"
    return net


