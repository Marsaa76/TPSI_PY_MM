def analyze_movie_archive(xml_content, xsd_content):
    with open("schema.xsd", "w") as xsd_file:
        xsd_file.write(xsd_content)
    schema = xmlschema.XMLSchema("schema.xsd")

    with open("document.xml", "w") as xml_file:
        xml_file.write(xml_content)

    if schema.is_valid("document.xml"):
        print("Documento XML valido!")
        root = etree.parse("document.xml").getroot()
        for movie in root.findall("movie"):
            title = movie.find("title").text
            reviews = movie.findall("reviews")
            total_rating = sum(int(review.find("rating").text) for review in reviews)
            avg_rating = total_rating / len(reviews)

            if avg_rating > 8:
                print(f"{title}: Average Rating {avg_rating:.1f}")
    else:
        print("Documento XML non valido!")