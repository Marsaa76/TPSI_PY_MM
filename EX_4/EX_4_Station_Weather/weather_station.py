def analizza_stazione_meteo(xml_content, xsd_content):
    with open("schema.xsd", "w") as xsd_file:
        xsd_file.write(xsd_content)
    schema = xmlschema.XMLSchema("schema.xsd")

    with open("document.xml", "w") as xml_file:
        xml_file.write(xml_content)

    if schema.is_valid("document.xml"):
        print("Documento XML valido!")
        root = etree.parse("document.xml").getroot()
        rilevazioni = root.findall("rilevazioni")

        somma_temp, somma_umidita, somma_pressione, somma_pioggia = 0, 0, 0, 0
        count = len(rilevazioni)

        for rilevazione in rilevazioni:
            somma_temp += float(rilevazione.find("temperatura").text)
            somma_umidita += int(rilevazione.find("umidita").text)
            somma_pressione += int(rilevazione.find("pressione").text)
            somma_pioggia += float(rilevazione.find("pioggia").text)

        print("Valori medi giornalieri:")
        print(f"Temperatura media: {somma_temp / count:.2f} °C")
        print(f"Umidità media: {somma_umidita / count:.2f} %")
        print(f"Pressione media: {somma_pressione / count:.2f} hPa")
        print(f"Pioggia media: {somma_pioggia / count:.2f} mm")
    else:
        print("Documento XML non valido!")

# Esempio di utilizzo
analizza_stazione_meteo(stazione_meteo_xml, stazione_meteo_xsd)
