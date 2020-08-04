# -*- coding: UTF-8 -*-

#!/usr/bin/python
# 
# Filename:  NavegacionWeb.py 
#
# Version: 1.0.0
#
# 
# 
#  Descripcion:  
# 
# Menu_principal.py contiene el menú desde el cuál se podrá lanzar toda la pila de módulos
# configurados para el agente, tendrá la posibilidad de listar los agentes junto con sus 
# configuraciones. Contará con la posibilidad de crear agentes nuevos y lanzar los existentes
# 
# 
#   
#
# Instrucciones
# 
# Para la ejecución del menú principal y empezar a la configuración del agente
# Es necesario ejecutar el archivo llamado Menu_principal.py como se muestra:
# Ejemplo:  
#
#   $ ./Menu_principal.py 

from colorama import init, Fore, Back, Style
import os, sys, getopt, datetime, time, random, importlib, json,ftplib, urllib


# ================================================================================================
#
# Función:  PornSites()
#
# Descripción:   Función que permite simular una navegación a sitios web con contenido para adultos
#               haciendo uso del dominio .xxx
#
# Parámetros: Ninguno
# 
#
# 
# 
# ================================================================================================

def PornSites():
    print("Entrando a guarrasdelporno.xxx")
    webSession = urllib.urlopen( 'http://guarrasdelporno.xxx', 'https://ipornovideos.xxx')
    trash =webSession.read()
    print("Entrando a gipornovideos.xxx")
    webSession1 = urllib.urlopen( 'https://ipornovideos.xxx')
    trash =webSession1.read()
    print("Entrando a drpornogratisx.xxx")
    webSession2 = urllib.urlopen( 'https://drpornogratisx.xxx')
    trash =webSession2.read()
    print("Entrando a veopornogratis.xxx")
    webSession3 = urllib.urlopen( 'https://veopornogratis.xxx')
    trash =webSession3.read()
    

def MaliciousSites():
    print("Navegación web por sitios maliciosos")
    