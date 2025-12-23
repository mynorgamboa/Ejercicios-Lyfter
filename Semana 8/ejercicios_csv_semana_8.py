# 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB

# import csv

# def get_video_games_info():
#     new_list = []
#     try:
#         amount = int(input('Cuantos juegos desea ingresar? '))
#         for index in range(0, amount):
#             new_dict = {}
#             name = input('Cual es el nombre del juego? ')
#             genre = input('Cual es el genero del juego? ')
#             developer = input('Cual es el desarrollador? ')
#             classification = input('Cual es la clasificación ESRB? ')
#             new_dict["name"] = name
#             new_dict["genre"] = genre
#             new_dict["developer"] = developer
#             new_dict["classification"] = classification
#             new_list.append(new_dict)
#         return new_list
#     except Exception as error:
#         print(f'Ha ocurrido un error en get_video_games_info(): {error}')


# def create_csv(csv_file, information, headers):
#     try:
#         with open(csv_file, 'w', encoding='UTF-8') as file:
#             writer = csv.DictWriter(file, headers)
#             writer.writeheader()
#             writer.writerows(information)
#     except Exception as error: 
#         print(f'Ha ocurrido un error en create_csv(): {error}')


# def main():
#     try:
#         important_list = get_video_games_info()
#         create_csv('videogames_list.csv', important_list, important_list[0].keys())
#     except Exception as error:
#         print(f'Ha ocurrido un error inesperado: {error}')


# main()

# Lea sobre el resto de métodos del módulo csv aqui 
# y cree una version alternativa del ejercicio de arriba 
# que guarde el archivo separado por tabulaciones en vez de por comas.

import csv

def get_video_games_info():
    new_list = []
    try:
        amount = int(input('Cuantos juegos desea ingresar? '))
        for index in range(0, amount):
            new_dict = {}
            name = input('Cual es el nombre del juego? ')
            genre = input('Cual es el genero del juego? ')
            developer = input('Cual es el desarrollador? ')
            classification = input('Cual es la clasificación ESRB? ')
            new_dict["name"] = name
            new_dict["genre"] = genre
            new_dict["developer"] = developer
            new_dict["classification"] = classification
            new_list.append(new_dict)
        return new_list
    except Exception as error:
        print(f'Ha ocurrido un error en get_video_games_info(): {error}')


def create_csv(csv_file, information, headers):
    try:
        with open(csv_file, 'w', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, headers, delimiter= '\t')
            writer.writeheader()
            writer.writerows(information)
    except Exception as error: 
        print(f'Ha ocurrido un error en create_csv(): {error}')


def main():
    try:
        important_list = get_video_games_info()
        create_csv('videogames_list.csv', important_list, important_list[0].keys())
    except Exception as error:
        print(f'Ha ocurrido un error inesperado: {error}')


main()