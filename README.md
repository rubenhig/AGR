# AGRp2
Práctica 2 de AGR
![alt text](https://github.com/rubenhig/AGR/blob/main/P2_net_diagram.png)

Para generar la red descrita en la imagen anterior, hay que tener montado el entorno correctamente.
### 1. Instalar dependencias: 
Primero las dependencias relacionadas con Qemu y KVM:
```
sudo apt install libvirt-clients libvirt-daemon-system
libvirt-daemon virtinst bridge-utils qemu qemu-kvm
sudo apt install virt-manager
sudo apt install ssh-askpass
```
Posteriormente, habrá que instalar las librerías usadas por el Script (lxml):
```
sudo apt install python3-lxml
```
o bien:
```
pip install lxml
```
Si al lanzar el script nos da error de permisos al intentar usar las imagenes .qcow, debemos editar el siguiente fichero: 
```
sudo nano /etc/libvirt/qemu.conf
```
y en la líneas
```
#user = "root"
...
#group = "libvirt"
```
las modificamos:
```
user = "alumno" (o el usuario que va a ejecutar el script)
...
group = "libvirt"
```



# AGRp3
![alt text](https://github.com/rubenhig/AGR/blob/main/net_diagram.PNG)



