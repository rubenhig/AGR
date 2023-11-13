from lxml import etree
import os

BASE_DISK_PATH = "/home/alumno/Descargas/disks/"
MASTER_DISK_PATH = "/home/alumno/Descargas/agr-vm-base.qcow2"


class XmlGenerator:
    def __init__(self, reference_path: str) -> None:
        self.reference_path = reference_path

    def generateXml(
        self, name: str, disk_path: str, xml_path: str, bridges: list
    ) -> None:
        """
        Crea ficheros xml para maquinas virtuales kvm

        Args:
            quantity (int): # de ficheros a generar
        """

        # Parse the XML file
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(self.reference_path, parser)
        # Get the root element of the XML
        root = tree.getroot()

        # Generate a random UUID
        root.find("name").text = name

        # Locate the <source> element you want to update
        source_element = root.find(".//disk[@type='file']/source")

        # Update the 'file' attribute's value
        source_element.set("file", disk_path)

        source_element = root.find(".//interface[@type='bridge']/source")
        source_element.set("bridge", bridges[0])

        if len(bridges) > 1:
            devices = root.find("devices")
            for bridge in bridges[1:]:
                bridge_element = etree.fromstring(
                    f'<interface type="bridge"><source bridge="{bridge}"/><model type="virtio"/></interface>'
                )
                devices.append(bridge_element)

        # Save the updated XML back to the file
        tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding="utf-8")


def main():
    xml_generator = XmlGenerator("./xml_reference.xml")

    # ============================== #
    #             Bridges            #
    # ============================== #

    bridge_Red1_Rc = "Red1"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Red1_Rc} down")
    os.system(f"sudo brctl delbr {bridge_Red1_Rc}")

    os.system(f"sudo brctl addbr {bridge_Red1_Rc}")
    os.system(f"sudo ifconfig {bridge_Red1_Rc} up")

    bridge_Red2_Rc = "Red2"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Red2_Rc} down")
    os.system(f"sudo brctl delbr {bridge_Red2_Rc}")

    os.system(f"sudo brctl addbr {bridge_Red2_Rc}")
    os.system(f"sudo ifconfig {bridge_Red2_Rc} up")

    bridge_Red3_Rd = "Red3"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Red3_Rd} down")
    os.system(f"sudo brctl delbr {bridge_Red3_Rd}")
    
    os.system(f"sudo brctl addbr {bridge_Red3_Rd}")
    os.system(f"sudo ifconfig {bridge_Red3_Rd} up")

    bridge_Red4_Rd = "Red4"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Red4_Rd} down")
    os.system(f"sudo brctl delbr {bridge_Red4_Rd}")

    os.system(f"sudo brctl addbr {bridge_Red4_Rd}")
    os.system(f"sudo ifconfig {bridge_Red4_Rd} up")

    bridge_Rc_Rb = "RcRb"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Rc_Rb} down")
    os.system(f"sudo brctl delbr {bridge_Rc_Rb}")

    os.system(f"sudo brctl addbr {bridge_Rc_Rb}")
    os.system(f"sudo ifconfig {bridge_Rc_Rb} up")

    bridge_Rd_Rb = "RbRd"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Rd_Rb} down")
    os.system(f"sudo brctl delbr {bridge_Rd_Rb}")

    os.system(f"sudo brctl addbr {bridge_Rd_Rb}")
    os.system(f"sudo ifconfig {bridge_Rd_Rb} up")

    bridge_Rb_Ra = "RbRa"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Rb_Ra} down")
    os.system(f"sudo brctl delbr {bridge_Rb_Ra}")

    os.system(f"sudo brctl addbr {bridge_Rb_Ra}")
    os.system(f"sudo ifconfig {bridge_Rb_Ra} up")

    bridge_Ra_Servidor = "SRa"

    # Borrar los bridges antes de volver a crearlos
    os.system(f"sudo ip link set {bridge_Ra_Servidor} down")
    os.system(f"sudo brctl delbr {bridge_Ra_Servidor}")

    os.system(f"sudo brctl addbr {bridge_Ra_Servidor}")
    os.system(f"sudo ifconfig {bridge_Ra_Servidor} up")

    # ============================== #
    #               pc0              #
    # ============================== #

    name = "pc0"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Red1_Rc])

    os.system(f"sudo virsh define {xml_path}")
     
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #               pc1              #
    # ============================== #

    name = "pc1"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Red2_Rc])

    os.system(f"sudo virsh define {xml_path}")
 
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #               pc2              #
    # ============================== #

    name = "pc2"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Red3_Rd])

    os.system(f"sudo virsh define {xml_path}")
     
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #               pc3              #
    # ============================== #

    name = "pc3"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Red4_Rd])

    os.system(f"sudo virsh define {xml_path}")
 
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #            Servidor            #
    # ============================== #

    name = "servidor"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Ra_Servidor])

    os.system(f"sudo virsh define {xml_path}")
 
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #               Ra               #
    # ============================== #

    name = "Ra"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Ra_Servidor, bridge_Rb_Ra])

    os.system(f"sudo virsh define {xml_path}")
     
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #               Rb               #
    # ============================== #

    name = "Rb"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Rb_Ra, bridge_Rc_Rb, bridge_Rd_Rb])

    os.system(f"sudo virsh define {xml_path}")
 
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #               Rc               #
    # ============================== #

    name = "Rc"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Rc_Rb, bridge_Red1_Rc, bridge_Red2_Rc])

    os.system(f"sudo virsh define {xml_path}")
     
    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

    # ============================== #
    #               Rd               #
    # ============================== #

    name = "Rd"
    disk_path = f"{BASE_DISK_PATH}{name}.qcow2"
    xml_path = f"./xml_machines/{name}.xml"
    os.system(f"qemu-img create -f qcow2 -b {MASTER_DISK_PATH} -F qcow2 {disk_path}")
    xml_generator.generateXml(name, disk_path, xml_path, bridges=[bridge_Rd_Rb, bridge_Red3_Rd, bridge_Red4_Rd])

    os.system(f"sudo virsh define {xml_path}")

    copy_to_interfaces(f'./interfaces/{name}')
    os.system(f'sudo virt-copy-in -a {disk_path} ./interfaces/interfaces /etc/network/')

    os.system(f"sudo virsh start {name}")

def copy_to_interfaces(input_path: str):
    os.system(f'cp {input_path} ./interfaces/interfaces')


if __name__ == "__main__":
    main() # TODO: Comprobar bridge Red 3 y 4
