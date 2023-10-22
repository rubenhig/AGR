#!/bin/bash

### Script encargado de descargar el codigo del servidor web, asi como todas sus dependencias ### 

git clone https://github.com/gisai/SSR-master-server.git
cd SSR-master-server/

sudo apt install -y nodejs 
sudo apt install -y npm

sudo npm install -g nodemon
sudo npm install

sed -i 's/3000/3001/g' app.js

npm start