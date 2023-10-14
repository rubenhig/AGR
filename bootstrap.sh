#!bin/bash

### Script encargado de descargar el codigo del servidor web, asi como todas sus dependencias ### 


sudo apt-get install nodejs
sudo apt-get install npm
cd $HOME
git clone "https://github.com/gisai/SSR-master-server.git"
cd ./SSR-master-server
npm install -g nodemon
npm install 
npm start