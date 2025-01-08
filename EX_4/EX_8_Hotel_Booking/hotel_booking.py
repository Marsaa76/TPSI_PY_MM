def analyze_hotel_bookings(xml_content, xsd_content):
    with open("schema.xsd", "w") as xsd_file:
        xsd_file.write(xsd_content)
    schema = xmlschema.XMLSchema("schema.xsd")

    with open("document.xml", "w") as xml_file:
        xml_file.write(xml_content)

    if schema.is_valid("document.xml"):
        print("Documento XML valido!")
        root = etree.parse("document.xml").getroot()

        total_occupancy = 0
        for booking in root.findall("bookings"):
            client = booking.find("client_name").text
            check_in = booking.find("check_in").text
            check_out = booking.find("check_out").text
            print(f"Prenotazione: {client} dal {check_in} al {check_out}")
            total_occupancy += 1

        print(f"Numero totale di prenotazioni: {total_occupancy}")
    else:
        print("Documento XML non valido!")