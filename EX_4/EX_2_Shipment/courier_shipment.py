from datetime import datetime

class Localita:
    def __init__(self, luogo, data_ora):
        self.luogo = luogo
        self.data_ora = datetime.fromisoformat(data_ora)

class Spedizione:
    def __init__(self):
        self.localita = []

    def aggiungi_localita(self, luogo, data_ora):
        self.localita.append(Localita(luogo, data_ora))

    def calcola_tempo_totale(self):
        if len(self.localita) >= 2:
            return (self.localita[-1].data_ora - self.localita[0].data_ora).total_seconds()
        return 0

    def genera_xml_tempi(self):
        root = etree.Element("spedizione")
        for i in range(len(self.localita) - 1):
            tempo = (self.localita[i + 1].data_ora - self.localita[i].data_ora).total_seconds()
            etree.SubElement(root, "tempo").text = str(int(tempo))
        return etree.tostring(root, pretty_print=True).decode()

# Esempio uso Spedizione
spedizione = Spedizione()
spedizione.aggiungi_localita("Pisa, aeroporto", "2022-03-07T12:00:15")
spedizione.aggiungi_localita("Pisa, stazione", "2022-03-07T18:00:30")
spedizione.aggiungi_localita("Livorno, stazione", "2022-03-07T22:15:45")

tempo_totale = spedizione.calcola_tempo_totale()
print(f"Tempo totale trascorso: {tempo_totale} secondi")

xml_tempi = spedizione.genera_xml_tempi()
print("XML con tempi tra località:")
print(xml_tempi)