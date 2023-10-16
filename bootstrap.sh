#!/bin/bash

### Script encargado de descargar el codigo del servidor web, asi como todas sus dependencias ### 

echo "export PORT=3001" >> /etc/profile.d/myvar.sh
sudo apt-get install -y nodejs
sudo apt-get install -y npm
sudo apt-get install -y git
echo "HEMOS INSTALADO NODEJS, GIT Y NPM"
git clone https://github.com/gisai/SSR-master-server.git
echo "git clone"
cd ./SSR-master-server
sudo npm install -g nodemon
sudo npm install 
sudo npm start