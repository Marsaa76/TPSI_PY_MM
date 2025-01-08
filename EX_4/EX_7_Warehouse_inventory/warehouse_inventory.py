def analyze_warehouse_inventory(xml_content, xsd_content):
    with open("schema.xsd", "w") as xsd_file:
        xsd_file.write(xsd_content)
    schema = xmlschema.XMLSchema("schema.xsd")

    with open("document.xml", "w") as xml_file:
        xml_file.write(xml_content)

    if schema.is_valid("document.xml"):
        print("Documento XML valido!")
        root = etree.parse("document.xml").getroot()

        for category in root.findall("categories"):
            category_name = category.find("category").text
            print(f"Categoria: {category_name}")

            total_value = 0
            for product in category.findall("products"):
                price = float(product.find("price").text)
                quantity = int(product.find("quantity").text)
                total_value += price * quantity

            print(f"Valore complessivo della categoria: {total_value:.2f}")
    else:
        print("Documento XML non valido!")
