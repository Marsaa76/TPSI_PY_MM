def validate_medical_results(xml_content, xsd_content):
    with open("schema.xsd", "w") as xsd_file:
        xsd_file.write(xsd_content)
    schema = xmlschema.XMLSchema("schema.xsd")

    with open("document.xml", "w") as xml_file:
        xml_file.write(xml_content)

    if schema.is_valid("document.xml"):
        print("Documento XML valido!")
        root = etree.parse("document.xml").getroot()
        for test in root.findall("test"):
            analysis = test.find("analysis").text
            result = float(test.find("result").text)
            reference_min = float(test.find("reference_min").text)
            reference_max = float(test.find("reference_max").text)

            if reference_min <= result <= reference_max:
                print(f"{analysis}: Risultato normale ({result})")
            else:
                print(f"{analysis}: Risultato fuori range ({result})")
    else:
        print("Documento XML non valido!")

# Esempio di utilizzo
validate_medical_results(medical_test_results_xml, medical_test_results_xsd)