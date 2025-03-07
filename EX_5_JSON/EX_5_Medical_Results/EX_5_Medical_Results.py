import json
import os
import jsonschema
from jsonschema import validate, ValidationError

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def compute_esito(risultato, intervallo):
    if risultato < intervallo["min"]:
        return "troppo basso"
    elif risultato > intervallo["max"]:
        return "valore elevato"
    else:
        return "ok"

def validate_esami(data, schema):
    validi = []
    non_validi = []
    
    for idx, esame in enumerate(data.get("esami", []), start=1):
        try:
            # Validazione iniziale tramite schema
            validate(instance=esame, schema=schema["properties"]["esami"]["items"])
            # Ricalcola l'esito (opzionale, per verificare la correttezza dei dati)
            esame["esito"] = compute_esito(esame["risultato"], esame["intervallo"])
            validi.append(esame)
        except ValidationError as e:
            print(f"Errore nel record esame {idx}: {e.message}")
            non_validi.append(esame)
    
    return validi, non_validi

def main():
    # Ottieni il percorso della directory dello script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Costruisci i percorsi completi dei file JSON e schema
    json_file_path = os.path.join(script_dir, "EX_5_Medical_Results.json")
    schema_file_path = os.path.join(script_dir, "EX_5_Medical_Results_schema.json")
    output_file_path = os.path.join(script_dir, "EX_5_Medical_Results_output.json")
    
    # Carica i dati e lo schema dai file JSON
    data = load_json(json_file_path)
    schema = load_json(schema_file_path)
    
    # Valida i record degli esami medici
    validi, non_validi = validate_esami(data, schema)
    
    print("\nEsami validi:")
    for esame in validi:
        print(f" - {esame['nome']} {esame['cognome']} ({esame['analisi']}): {esame['risultato']} {esame['unita']} => {esame['esito']}")
    
    print("\nEsami NON validi:")
    for esame in non_validi:
        print(f" - {esame.get('nome', 'Nome mancante')} {esame.get('cognome', 'Cognome mancante')}")
    
    # Salva i record validi in un nuovo file JSON
    output_data = {"esami": validi}
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    print(f"\nRecord validi salvati in '{output_file_path}'.")

if __name__ == "__main__":
    main()
