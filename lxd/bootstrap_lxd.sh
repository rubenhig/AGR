#!/bin/bash

### Script encargado de descargar el codigo del servidor web, asi como todas sus dependencias ### 

sudo apt update -y

sudo apt install -y nodejs
sudo apt install -y npm
sudo apt install -y git
echo "HEMOS INSTALADO NODEJS, GIT Y NPM"
git clone https://github.com/gisai/SSR-master-server.git
echo "git clone"
cd ./SSR-master-server
sudo npm install -g nodemon
sudo npm install 
sed -i 's/3000/3001/g' app.js
sudo npm start