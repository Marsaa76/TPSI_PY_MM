import time

def analizza_trasporto(xml_content, xsd_content, soglia_temperatura):
    with open("schema.xsd", "w") as xsd_file:
        xsd_file.write(xsd_content)
    schema = xmlschema.XMLSchema("schema.xsd")

    with open("document.xml", "w") as xml_file:
        xml_file.write(xml_content)

    if schema.is_valid("document.xml"):
        print("Documento XML valido!")
        root = etree.parse("document.xml").getroot()
        for veicolo in root.findall("veicolo"):
            id_veicolo = veicolo.find("ID").text
            misure = veicolo.findall("misura")
            superata_soglia = False
            timestamp_superati = []

            for misura in misure:
                temperatura = float(misura.find("temperatura").text)
                data_ora = misura.find("data_ora").text
                timestamp = int(datetime.fromisoformat(data_ora).timestamp())

                if temperatura > soglia_temperatura:
                    superata_soglia = True
                    timestamp_superati.append(timestamp)

            print(f"Veicolo ID: {id_veicolo}")
            print(f"Tutte temperature sotto soglia: {not superata_soglia}")
            if timestamp_superati:
                print(f"Timestamp sopra soglia: {timestamp_superati}")
    else:
        print("Documento XML non valido!")

# Esempio di utilizzo
analizza_trasporto(trasporto_congelati_xml, trasporto_congelati_xsd, -30.0)