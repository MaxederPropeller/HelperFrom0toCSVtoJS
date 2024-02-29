import csv

def csv_to_js(csv_file_path, js_file_path, js_var_name='data'):
    records = []

    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Konvertiert jedes Dictionary (Zeile) in ein JS-Objekt-String-Format
            record_js = '{' + ', '.join([f"{key}: {repr(str(value))}" for key, value in row.items()]) + '}'
            records.append(record_js)

    # Die Daten als JS-Array von Objekten in einer .js-Datei speichern
    with open(js_file_path, mode='w', encoding='utf-8') as js_file:
        js_file.write(f"const {js_var_name} = [\n  " + ',\n  '.join(records) + "\n];\n")
        js_file.write(f"export default {js_var_name};")

csv_file_path = 'C:\\Users\\Max\\Desktop\\newData.csv'
js_file_path = 'C:\\Users\\Max\\Desktop\\DeportFinish.csv'

csv_to_js(csv_file_path, js_file_path)
