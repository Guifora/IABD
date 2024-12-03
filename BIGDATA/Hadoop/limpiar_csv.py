import csv
import re

# Leer el archivo CSV original
with open('marvel_movies.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Función para procesar cada fila del CSV
def process_row(row):
    processed_row = []
    for i, cell in enumerate(row):
        if cell.startswith('"') and cell.endswith('"'):
            # Si la celda está entre comillas, procesa el contenido
            content = cell[1:-1]  # Elimina las comillas
            processed_content = re.sub(r'(\d+,\.\d+)', lambda m: m.group(0).replace(',', '.'), content)
            processed_row.append(f'"{processed_content}"')
        else:
            processed_row.append(cell)
    return processed_row

# Procesar cada fila del CSV
processed_data = [process_row(row) for row in data]

# Escribir el resultado en un nuevo archivo CSV
with open('marvel_movies_processed.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(processed_data)

print("Proceso completado. El archivo procesado se ha guardado como marvel_movies_processed.csv")