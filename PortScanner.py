#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)
remoteServer    = raw_input("Ingresa una direccion IP o un rango valido: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
print "-" * 60
print "Escaneando objetivo", remoteServerIP
print "-" * 60

# Fecha de escaneo
t1 = datetime.now()

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Puerto {}: 	 Abierto".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Bye"
    sys.exit()

except socket.gaierror:
    print 'Host no identificado'
    sys.exit()

except socket.error:
    print "Imposible conectar"
    sys.exit()
t2 = datetime.now()
total =  t2 - t1
print 'Fin: ', total