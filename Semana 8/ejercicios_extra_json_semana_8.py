# 1. Cree un programa que abra un archivo `.json` 
# con la información de Pokémon 
# ( en base al JSON que fue generado en el ejercicio 1) y:
# - Lea el archivo `JSON` de Pokémon
# - Recorra la lista de Pokémon y 
# muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

# import json

# def open_pokemons(path):
#     try:
#         with open(path, 'r') as file: 
#             pokemon_list = json.load(file)
#         return pokemon_list
#     except Exception as error:
#         print(f'Ha ocurrido un error en open_pokemons(): {error}')


# def show_pokemons(pokemon_list):
#     all_types = ""
#     try:
#         for index in pokemon_list:
#             for key,value in index.items():
#                 if (key == "name"):
#                     for names in value.values():
#                         print(f'{key}: {names}')
#                 elif (key == "type"):
#                     for type in value:
#                         if (len(value) != 1) :
#                             all_types += type + " "
#                         else:
#                             all_types=type
#                     print(f'{key}: {all_types}')
#                     all_types = ""
#                 else:
#                     for bases,amount in value.items():
#                         print(f'{bases}: {amount}')
#             print('*'*30)
#     except Exception as error:
#         print(f'Ha ocurrido un error en show_pokemons(): {error}')


# def main():
#     try:
#         final_list = open_pokemons("pokemons.json")
#         show_pokemons(final_list)
#     except Exception as error:
#         print(f'Ha ocurrido un error inesperado: {error}')

# main()


# 1. Cree un programa que abra un archivo `.json` 
# con la información de Pokémon 
# ( en base al JSON que fue generado en el ejercicio 1) y:
# - Lea el archivo `JSON` de Pokémon
# - Pida al usuario un tipo de Pokémon
# - Muestre todos los Pokémon que sean de ese tipo


import json


def open_pokemons(route):
    try:
        with open(route, 'r') as file:
            opened = json.load(file)
        return opened
    except Exception as error: 
        print(f'Ha ocurrido un error en open_pokemons(): {error}')


def get_pokemon_type(): 
    pokemon_type = ""
    types = (
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
    "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
    "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy")
    try:
        while (pokemon_type not in types):
            new_type = input('Pokemon type? ')
            pokemon_type = new_type
            if (pokemon_type in types):
                return pokemon_type
            else:
                print("This type doesn't exist, give me a real one and use Capital !")
    except Exception as error: 
        print(f'Ha ocurrido un error en get_pokemon_type(): {error}')


def show_pokemons(list_pokemon,pokemon_type):
    matched = []
    try:
        for pokemon in list_pokemon:
            for key, value in pokemon.items():
                # print(f'Key: {key}\n Value: {value}\n Matched: {matched}')
                if (key == "type" and pokemon_type in value):
                    # print(pokemon["name"]["english"])
                    matched.append(pokemon["name"]["english"])
        print(f'Los pokemons con ese tipo son:')
        for final in matched:
            print(final)
    except Exception as error: 
        print(f'Ha ocurrido un error en show_pokemons(): {error}')


def main():
    try:
        pokemon_type = get_pokemon_type()
        opened = open_pokemons('pokemons.json')
        show_pokemons(opened,pokemon_type)
    except Exception as error: 
        print(f'Ha ocurrido un error inesperado: {error}')

main()