from lxml import etree
import uuid


class MacGenerator:
    def __init__(self) -> None:
        self.sequence = 0

    def generate_mac_address(self) -> str:
        """
        Generate a MAC address based on a sequence number.

        Args:
            sequence (int): The sequence number.

        Returns:
            str: A MAC address string.
        """
        # Ensure the sequence number is within a valid range (0x00 to 0xFF)
        if 0 <= self.sequence <= 255:
            mac_address = "52:54:00:{:02X}:00:00".format(self.sequence)
            self.sequence += 1
            return mac_address


class XmlGenerator:
    def __init__(self, reference_path: str, base_name: str) -> None:
        self.reference_path = reference_path
        self.base_name = base_name
        self.mac_generator = MacGenerator()
        self.counter = 0

    def generateXml(self, quantity: int) -> None:
        """Crea ficheros xml para maquinas virtuales kvm

        Args:
            quantity (int): # de ficheros a generar
        """

        for _ in range(quantity):
            # Parse the XML file
            tree = etree.parse(self.reference_path)
            # Get the root element of the XML
            root = tree.getroot()

            # Generate a random UUID
            new_name = f"{self.base_name}_{self.counter:02}"
            root.find("name").text = new_name
            root.find("uuid").text = f"{uuid.uuid4()}"

            # Locate the <source> element you want to update
            source_element = root.find(".//disk[@type='file']/source")

            # Update the 'file' attribute's value
            source_element.set("file", "/route/to/new/disk")

            # Locate the <mac> element you want to update
            mac_element = root.find(".//interface[@type='network']/mac")

            # Update the text content of the <mac> element with the new MAC address
            new_mac_address = self.mac_generator.generate_mac_address()
            mac_element.set("address", new_mac_address)

            # Save the updated XML back to the file
            tree.write(f"./out/{new_name}.xml", pretty_print=True)
            self.counter += 1


def main():
    # Specify the path to your XML file
    xml_file_path = "./xml_reference.xml"
    xml_gen = XmlGenerator(xml_file_path, "vm")

    xml_gen.generateXml(3)


if __name__ == "__main__":
    main()
