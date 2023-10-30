from lxml import etree
import uuid
import os

BASE_DISK_PATH = '/home/alumno/Descargas/disks/'
MASTER_DISK_PATH = '/home/alumno/Descargas/agr-vm-base.qcow2'

class XmlGenerator:
    def __init__(self, reference_path: str) -> None:
        self.reference_path = reference_path

    def generateXml(self, name: str, disk_path: str, xml_path: str, bridge: str) -> None:
        """
        Crea ficheros xml para maquinas virtuales kvm

        Args:
            quantity (int): # de ficheros a generar
        """

        # Parse the XML file
        tree = etree.parse(self.reference_path)
        # Get the root element of the XML
        root = tree.getroot()

        # Generate a random UUID
        root.find("name").text = name

        # Locate the <source> element you want to update
        source_element = root.find(".//disk[@type='file']/source")

        # Update the 'file' attribute's value
        source_element.set("file", disk_path)

        source_element = root.find(".//interface[@type='bridge']/source")
        source_element.set("bridge", bridge)

        # Save the updated XML back to the file
        tree.write(xml_path, pretty_print=True)


def main():
    xml_generator = XmlGenerator('./xml_reference.xml')
    
    # ============================== #
    #             Bridges            #
    # ============================== #

    bridge_Red1_Rc = 'bridgeRed1'
    os.system(f'sudo brctl addbr {bridge_Red1_Rc}')
    os.system(f'sudo ip config {bridge_Red1_Rc} 10.0.0.0/24')
    os.system(f'sudo ip config {bridge_Red1_Rc} up')

    bridge_Red2_Rc = 'bridgeRed2'
    os.system(f'sudo brctl addbr {bridge_Red2_Rc}')
    os.system(f'sudo ip config {bridge_Red2_Rc} 10.0.1.0/24')
    os.system(f'sudo ip config {bridge_Red2_Rc} up')

    bridge_Red3_Rd = 'bridgeRed3'
    os.system(f'sudo brctl addbr {bridge_Red3_Rd}')
    os.system(f'sudo ip config {bridge_Red3_Rd} 10.0.2.0/24')
    os.system(f'sudo ip config {bridge_Red3_Rd} up')

    bridge_Red4_Rd = 'bridgeRed4'
    os.system(f'sudo brctl addbr {bridge_Red4_Rd}')
    os.system(f'sudo ip config {bridge_Red4_Rd} 10.0.3.0/24')
    os.system(f'sudo ip config {bridge_Red4_Rd} up')

    bridge_Rc_Rb = 'bridgeRcRb'
    os.system(f'sudo brctl addbr {bridge_Rc_Rb}')
    os.system(f'sudo ip config {bridge_Rc_Rb} 10.0.4.0/30')
    os.system(f'sudo ip config {bridge_Rc_Rb} up')

    bridge_Rd_Rb = 'bridgeRbRd'
    os.system(f'sudo brctl addbr {bridge_Rd_Rb}')
    os.system(f'sudo ip config {bridge_Rd_Rb} 10.0.4.4/30')
    os.system(f'sudo ip config {bridge_Rd_Rb} up')

    bridge__Rb_Ra = 'bridgeRbRd'
    os.system(f'sudo brctl addbr {bridge__Rb_Ra}')
    os.system(f'sudo ip config {bridge__Rb_Ra} 10.0.4.8/30')
    os.system(f'sudo ip config {bridge__Rb_Ra} up')

    bridge_Ra_Servidor = 'bridgeServidorRa'
    os.system(f'sudo brctl addbr {bridge_Ra_Servidor}')
    os.system(f'sudo ip config {bridge_Ra_Servidor} 10.0.4.12/30')
    os.system(f'sudo ip config {bridge_Ra_Servidor} up')

    # ============================== #
    #               pc0              #
    # ============================== #

    name = 'pc0'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path, bridge=bridge_Red1_Rc)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #               pc1              #
    # ============================== #

    name = 'pc1'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path, bridge=bridge_Red2_Rc)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #               pc2              #
    # ============================== #


    name = 'pc2'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path, bridge=bridge_Red2_Rc)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #               pc3              #
    # ============================== #


    name = 'pc3'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path, bridge=bridge_Red3_Rd)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #            Servidor            #
    # ============================== #


    name = 'servidor'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path, bridge=bridge_Ra_Servidor)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #               Ra               #
    # ============================== #


    name = 'Ra'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #               Rb               #
    # ============================== #


    name = 'Rb'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #               Rc               #
    # ============================== #


    name = 'Rc'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')

    # ============================== #
    #               Rd               #
    # ============================== #


    name = 'Rd'
    disk_path = f'{BASE_DISK_PATH}{name}.qcow2'
    xml_path = f'./xml_machines/{name}.xml'
    os.system(f'qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}')
    xml_generator.generateXml(name, disk_path, xml_path)

    os.system(f'sudo virsh define {xml_path}')
    os.system(f'sudo virsh start {name}')





if __name__ == "__main__":
    main()
