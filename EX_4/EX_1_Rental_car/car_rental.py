import xmlschema
from lxml import etree

def validate_and_filter(xml_content, xsd_content, classe_specifica):
    with open("schema.xsd", "w") as xsd_file:
        xsd_file.write(xsd_content)
    schema = xmlschema.XMLSchema("schema.xsd")

    with open("document.xml", "w") as xml_file:
        xml_file.write(xml_content)

    if schema.is_valid("document.xml"):
        print("Documento XML valido!")
        root = etree.parse("document.xml").getroot()
        alimentazione = root.find("alimentazione").text
        if alimentazione == "ibrida" and root.find("classe").text == classe_specifica:
            agenzie = root.findall("agenzie")
            for agenzia in agenzie:
                print(f"Agenzia: {agenzia.attrib['denominazione']} - Città: {agenzia.attrib['citta']}")
    else:
        print("Documento XML non valido!")

# Esempio di utilizzo
validate_and_filter(car_rental.xml, car_rental.xsd, "B")