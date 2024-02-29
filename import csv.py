import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    # JSON-Daten laden
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Überprüfen, ob die Daten korrekt formatiert sind
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON-Daten müssen eine Liste von Dictionaries sein.")
    
    # Alle einzigartigen Schlüssel sammeln
    fieldnames = set()
    for item in data:
        fieldnames.update(item.keys())
    
    # CSV-Datei schreiben
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=sorted(list(fieldnames)))
        writer.writeheader()
        for item in data:
            writer.writerow(item)

# Pfad zu deiner JSON- und CSV-Datei
json_file_path = 'C:\\Users\\Max\\Desktop\\normalizedData.json'
csv_file_path = 'C:\\Users\\Max\\Desktop\\PortToCSV.csv'


# Funktion aufrufen
json_to_csv(json_file_path, csv_file_path)
