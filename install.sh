#!/bin/bash
########### Variables globales##############
_INSTALL_NMAP=true


input="logo.dat"
echo Bienvenido al instalador de Tezcaltipoca, simulador de adversarios
while IFS= read -r line
do
  echo "$line"
done < "$input"
if [ "$EUID" -ne 0 ]
  then echo "Please, run as root"
  exit 1
fi
#Instalación de dependencias.
printf " System Update\n"
apt update
printf " System Upgrade\n"
apt upgrade
printf " Install Nmap Scanner \n"
apt install nmap
