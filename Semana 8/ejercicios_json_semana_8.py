# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON
#     1. Debe leer el archivo para importar los Pokemons existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

pokemons = [
  {
    "name": {
      "english": "Pikachu"
    },
    "type": [
      "Electric"
    ],
    "base": {
      "HP": 35,
      "Attack": 55,
      "Defense": 40,
      "Sp. Attack": 50,
      "Sp. Defense": 50,
      "Speed": 90
    }
  },
  {
    "name": {
      "english": "Charmander"
    },
    "type": [
      "Fire"
    ],
    "base": {
      "HP": 39,
      "Attack": 52,
      "Defense": 43,
      "Sp. Attack": 60,
      "Sp. Defense": 50,
      "Speed": 65
    }
  },
  {
    "name": {
      "english": "Squirtle"
    },
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
  }
]


def convert_json_to_python(path):
    try:
        with open(path, "r") as file:
            converted = json.load(file)
            print(converted)
            return converted
    except Exception as error: 
        print(f'An error occurred in convert_json_to_python(): {error}')


def create_pokemon_list():
    pokemon_list = {}
    type_list = []
    base_dict = {}
    languages = {}
    try:
        name = input("What's the Pokemon name? ")
        languages["english"] = name
        pokemon_list["name"] = languages
        types_amount = int(input("How many types does the Pokemon have? "))
        if (types_amount > 1 and types_amount <= 2):
            for index in range(0, types_amount):
                new_type = input(f"What's the Pokemon type {index+1}? ")
                type_list.append(new_type)
                print(f"Type {new_type} added successfully!")
        else:
            new_type = input(f"What's the Pokemon type? ")
            type_list.append(new_type)
            print(f"Type {new_type} added successfully!")
        pokemon_list["type"] = type_list
        HP_pokemon = int(input("What's the Pokemon HP? "))
        attack_pokemon = int(input("What's the Pokemon Attack? "))
        defense_pokemon = int(input("What's the Pokemon Defense? "))
        sp_attack_pokemon = int(input("What's the Pokemon Sp. Attack? "))
        sp_defense_pokemon = int(input("What's the Pokemon Sp. Defense? "))
        speed_pokemon = int(input("What's the Pokemon Speed? "))
        base_dict["HP"] = HP_pokemon
        base_dict["Attack"] = attack_pokemon
        base_dict["Defense"] = defense_pokemon
        base_dict["Sp. Attack"] = sp_attack_pokemon
        base_dict["Sp. Defense"] = sp_defense_pokemon
        base_dict["Speed"] = speed_pokemon
        pokemon_list["base"] = base_dict
        print(pokemon_list)
        return pokemon_list
    except ValueError as error:
        print('Only numbers please!!') 
    except IndexError as error:
        print('Only can have 2 types!!')
    except Exception as error:
        print(f'An error occurred in create_pokemon_list(): {error}')


def add_new_pokemon(original, added, path):
    try:
      original.append(added)
      print(original)
      with open(path, "w") as file:
        json.dump(original, file, indent=4)
    except Exception as error:
      print(f'An error occurred in add_new_pokemon(): {error}')


def main():
    try:
      original_json = convert_json_to_python("pokemons.json")
      new_pokemon = create_pokemon_list()
      add_new_pokemon(original_json,new_pokemon, "pokemons.json")
    except Exception as error:
      print(f'An unexpected error occurred: {error}')

main()