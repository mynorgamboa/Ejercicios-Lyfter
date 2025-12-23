# 1. Cree un programa que abra un archivo `.csv` 
# con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# - Lea cada línea usando `csv.reader()`
# - Muestre el contenido en pantalla de forma legible, línea por línea


import csv


def csv_reader(csv_file):
    keys_list = []
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # primera fila
            for index in reader:
                if keys_list == []:
                    keys_list = index
                else:
                    fila = dict(zip(keys_list, index))
                    for key, value in fila.items():
                        print(f"{key}: {value}")
    except Exception as error:
        print(f'Hubo un error en csv_reader(): {error}')


def main():
    try:
        csv_reader('videogames_list.csv')
    except Exception as error:
        print(f'Hubo un error inesperado: {error}')

main()