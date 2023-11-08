#!/bin/bash

###### Script encargado de lanzar un contenedor con LXD y ejecutar el servidor web con nodejs usando el fichero boostrap.sh ######

# 1. Hay que tener instalado LXD:

# sudo apt update -y
# sudo apt install snapd -y 

# 2. Inicializamos LXD: 
lxd init --minimal

# 3. Lanzamos un contenedor: 
lxc launch ubuntu:22.04 webServer

# 4. Movemos y ejecutamos dentro del contenedor el script bootstrap.sh
lxc file push --recursive ./bootstrap_lxd.sh webServer/home/ubuntu
lxc exec webServer -- sh /home/ubuntu/bootstrap_lxd.sh