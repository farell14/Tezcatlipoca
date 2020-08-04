# -*- coding: UTF-8 -*-

#!/usr/bin/python
# 
# Filename:  Menu_principal.py 
#
# Version: 1.0.1
#
# 
# 
#  Descripcion:  
# 
# Menu_principal.py contiene el menú desde el cuál se podrá lanzar toda la pila de módulos
# configurados para el agente, tendrá la posibilidad de listar los agentes junto con sus 
# configuraciones. Contará con la posibilidad de crear agentes nuevos y lanzar los existentes.
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

import NavegacionWeb
import NetworkScanning
import Accountdiscover
import UDP_connections
import threading
import getinfo
import AccountBruteforce





# ================================================================================================
#
# Función:      main_menu()
#
# Descripción:  Función que lanza el menú principal de la aplicación
# Contiene todas las categorías que es posible seleccionar mediante la entrada de usuario
# Contiene un validador de entradas de usuario.
#
# ================================================================================================



def main_menu():
    print (Fore.BLUE+"\n 1.- Network Scanning ")
    print (Fore.BLUE+"\n 2.- Account Bruteforce")
    print (Fore.BLUE+"\n 3.- Web surfing")
    print (Fore.BLUE+"\n 4.- Account Discover")
    print (Fore.BLUE+"\n 5.- Malware Emulation")
    print (Fore.BLUE+"\n 6.- Ejecutar Análisis completo")
    print (Fore.BLUE+"\n 7.- Ayuda") 
    print (Fore.BLUE+"\n 8.- Salir")
    print (Fore.BLUE+"\n     Ingresa una opción")
    seleccionInvalida=1
    while (seleccionInvalida):
        try:
            op=input(Fore.WHITE+'~ $ ')
            if(op> 0 and op <9):
                seleccionInvalida=0
            else:
                print("Seleccion inválida, Intenta nuevamente")
        except ValueError:
            print("Seleccion inválida, Intenta nuevamente")
    return op



# ================================================================================================
#
# Función:  ConstruirAgente()
#
# Descripción:   Función que permite crear agentes personalizados, que permite seleccionar 
# funciones desde las categorías existentes.
# 
#
# ================================================================================================

def ConstruirAgente():
    print("")
    NewAgent=simulador()
    NewAgent.nombre="sin título"
    
    continuar = raw_input("¿Continuar construyendo este módulo? [s/n]: ")
    

# ================================================================================================
#
# Función:  AgregarCategorias()
#
# Descripción:   Función que permite agregar categorías de ataque existentes al agente  
# recientemente creado, entre las categorías sobresalientes están:
#
# Malware
# Escaneo
# Navegación Web
# 
# ================================================================================================


def AgregarCategorias(thisAgent):
    print("")
    done=False
    contador=0
    






# ================================================================================================
#
# Función:  AccountBruteforce()
#
# Descripción:   Función que permite hacer un intento de conexión a un servicio FTP
#               utilizando nombres de usuario utilizados por defecto y una lista de
#               100 contraseñas comunes.
#
# Parámetros: Recibe como parámetro una dirección IP:
# 
#
# 
# 
# ================================================================================================

def AccountBruteforce(direccion_IP):
    print("")
    




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
    webSession = urllib.urlopen( 'http://guarrasdelporno.xxx')
    trash =webSession.read()
    print("Entrando a gipornovideos.xxx")
    webSession = urllib.urlopen( 'https://ipornovideos.xxx')
    trash =webSession.read()
    print("Entrando a drpornogratisx.xxx")
    webSession = urllib.urlopen( 'https://drpornogratisx.xxx')
    trash =webSession.read()
    print("Entrando a veopornogratis.xxx")
    webSession = urllib.urlopen( 'https://veopornogratis.xxx')
    trash =webSession.read()
    


if __name__ == '__main__':
    logo=open("logo.dat","r")
    op=None
    if(logo.mode=="r"):
        content=logo.read()
        print(Fore.GREEN+content)
    logo.close()
    print(Fore.RED+"\n Bienvenido a Tezcatlipoca, simulación de adversarios \n \n")
    #targetIP = raw_input("Ingresa la dirección IP o el segmento de red a analizar:")
    op=main_menu()
    if (op==1):
        header=open("network-scans.dat","r")
        if(header.mode=="r"):
            content=header.read()
            print(Fore.WHITE+content)
        header.close()
        op=input("$_ ")
    if(op==2):
        print("")
        header=open("account-bruteforce.dat","r")
        if(header.mode=="r"):
            content=header.read()
            print(Fore.WHITE+content)
        header.close()
    if(op==3):
        print("")
        header=open("websurfing.dat","r")
        if(header.mode=="r"):
            content=header.read()
            print(Fore.WHITE+content)
        header.close()
    if(op==4):
        print("")
        header=open("account-discover.dat","r")
        if(header.mode=="r"):
            content=header.read()
            print(Fore.WHITE+content)
        header.close()
    if(op==5):
        print("")
        header=open("malware.dat","r")
        if(header.mode=="r"):
            content=header.read()
            print(Fore.WHITE+content)
        header.close()
    if(op==6):
        print("")
        header=open("full.dat","r")
        if(header.mode=="r"):
            content=header.read()
            print(Fore.WHITE+content)
        header.close()
        selection=getinfo.menu()
        if(selection==1):
            IP=getinfo.manual()
            NetworkScanning.PortDiscover(IP)
            NetworkScanning.top1000(IP)
            NetworkScanning.SMBScann(IP)
            NavegacionWeb.PornSites()
            NetworkScanning.VulnsScan(IP)
            Accountdiscover.SMBDiscover(IP)
            Accountdiscover.TelnetDiscover(IP)
            Accountdiscover.FTPDiscover(IP)
            #AccountBruteforce.FTPBruteforce(IP)
            #AccountBruteforce.sshBruteforce(IP)
            print("Intentando acceder al FTP")
            orden="hydra -l root -P passwd.dat ftp://10.30.12.122"
            os.system(orden)
            print("Intentando acceder vía Secure Shell")
            orden="hydra -l root -p passwd.dat 10.30.12.229 -t 4 ssh"
            os.system(orden)
            #NetworkScanning.SMBScann(IP)


        if(selection==2):
            IP=getinfo.automatico()
            print(IP)
            NetworkScanning.PortDiscover(IP)
            NetworkScanning.top1000(IP)
            NetworkScanning.SMBScann(IP)
            NavegacionWeb.PornSites()


    if(op==7):
        print("")
        header=open("help.dat","r")
        if(header.mode=="r"):
            content=header.read()
            print(Fore.WHITE+content)
        header.close()
    if(op==8):
        print("Bye!")
        exit()
    

    #UDP_connections.requests(targetIP)
    #NetworkScanning.PortDiscover(targetIP)
    #NetworkScanning.VulnsScan(targetIP)
