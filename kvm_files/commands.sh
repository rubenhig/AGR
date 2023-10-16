# primero instalamos librerias: 
sudo apt install libvirt-clients libvirt-daemon-system libvirt-daemon virtinst bridge-utils qemu qemu-kvm
sudo apt install virt-manager
sudo apt install ssh-askpass

# probar que kvm funciona correctamente: 
sudo kvm-ok
systemctl status libvirtd

# creamos la maquina virtual de referencia (es mejor hacerlo desde la interfaz grafica de virt-manager): 
sudo virt-install --name=debian-vm \
os-type=Linux \
os-variant=alpinelinux3.7 \
vcpu=1 \
ram=1024 \
disk path=/var/lib/libvirt/images/Debian.img,size=15 \
graphics spice \
location=/home/lab/Downloads/alpine-extended-3.18.4-x86_64.iso \

# el login es 'root' sin contraseña

# si queremos copiar el xml de la maquina que hemos creado: 
sudo virsh list
sudo virsh dumpxml <id> > config_vm.xml

# ahora toca hacer el script que genere el resto de maquinas virtuales
cp config_vm.xml config_router_1.xml
qemu-img create -f qcow2 -b /var/lib/libvirt/images/reference.qcow2 /var/lib/libvirt/images/router_1.qcow2

# Cambiar el nombre de la máquina en <name>
# Cambiar la ruta de la imagen de disco en <source file>
# Cambiar el identificador en <uuid>
# CUIDADO: Los UUID siguen una estructura, utiliza el comando
# uuidgen para obtener uno nuevo para la máquina
# Cambiar la dirección MAC Libremente 

### Hay un ejemplo editado: config_router_1.xml ###
