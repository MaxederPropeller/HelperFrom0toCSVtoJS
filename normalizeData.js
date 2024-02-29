
const fs = require('fs');

function normalizeData(items) {
  const allKeys = new Set();
  
  items.forEach(item => {
    Object.keys(item).forEach(key => allKeys.add(key));
  });

  return items.map(item => {
    const normalizedItem = {};
    allKeys.forEach(key => {
      normalizedItem[key] = item.hasOwnProperty(key) ? item[key] : "";
    });
    return normalizedItem;
  });
}

// Angenommen, liquorProducts ist deine Datenliste
const normalizedData = normalizeData(liquorProducts);

// Überprüfung, ob alle Datensätze verarbeitet wurden
if (normalizedData.length === liquorProducts.length) {
  console.log("Alle Datensätze wurden erfolgreich verarbeitet.");
  // Die normalisierte Liste in eine Datei schreiben
  fs.writeFile('normalizedData.json', JSON.stringify(normalizedData, null, 2), (err) => {
    if (err) throw err;
    console.log('Die normalisierte Liste wurde in normalizedData.json gespeichert.');
  });
} else {
  console.log("Einige Datensätze wurden möglicherweise nicht verarbeitet.");
}
