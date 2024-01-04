#!/bin/bash

######
###### Script encargado de lanzar un contenedor con LXD y ejecutar el servidor web 
###### con nodejs usando el fichero boostrap.sh 
######

# 2. Inicializamos LXD: 
lxd init --minimal

# 3. Lanzamos un contenedor: 
lxc launch ubuntu:22.04 webServer
echo "stopping webServer..." 
lxc stop webServer --force
echo "webServer stopped"
echo "configuring webServer network..."
lxc network attach lxdbr0 webServer eth0 eth0
lxc config device set webServer eth0 ipv4.address 10.143.214.2
echo "webServer IP: 10.143.214.2"
lxc start webServer
echo "webServer started"

# 4. Movemos y ejecutamos dentro del contenedor el script bootstrap.sh
echo "Pushing bootstrap_lxd.sh..."
lxc file push --recursive ./bootstrap_lxd.sh webServer/.
echo "Executing bootstrap_lxd.sh"
lxc exec webServer -- sh /bootstrap_lxd.sh 