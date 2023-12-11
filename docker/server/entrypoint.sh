#!/bin/bash

### Script encargado de descargar el codigo del servidor web, asi como todas sus dependencias ### 
apt update -y
apt upgrade -y 

apt install -y nodejs
apt install -y npm
apt install -y git
echo "HEMOS INSTALADO NODEJS, GIT Y NPM"
git clone https://github.com/gisai/SSR-master-server.git
echo "git clone"
cd ./SSR-master-server
npm install -g nodemon
npm install 
sed -i 's/3000/3001/g' app.js

ip route change default via 10.5.0.1
npm start