#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#    - `nombre`
#    - `numero_de_estrellas`
#    - `habitaciones`
#El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información: numero, piso, precio por noche

#hotel_dictionary = {}
#rooms_list = []
#hotel_name = input("Cual es el nombre del hotel? ")
#stars_number = int(input("Cuantas estrellas tiene? "))
#rooms = int(input("Cuantas habitaciones tiene? "))

#hotel_dictionary["nombre"] = hotel_name
#hotel_dictionary["numero_de_estrellas"] = stars_number

#for index in range(0, rooms):
#    room_dictionary = {}
#    room_number = int(input(f"Cual es el numero del cuarto {index+1}? "))
#    floor_number = int(input("Cual es el numero del piso? "))
#    price_by_night = float(input("Cual es el precio por noche? "))

#    room_dictionary["numero"] = room_number
#    room_dictionary["piso"] = floor_number
#    room_dictionary["precio_por_noche"] = price_by_night
#    print(room_dictionary)

#    rooms_list.append(room_dictionary)

#    print(rooms_list)

#hotel_dictionary[f"habitaciones"] = rooms_list

#print(hotel_dictionary)





#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

#two_list_dictionary = {}
#first_list = []
#second_list = []

#amount_values = int(input("Cuantos datos va a guardar en el diccionario? "))

#for index in range (0,amount_values):
#    new_key = input("Cual es el dato a guardar? ")
#    first_list.append(new_key)
#    value_for_key = input(f"Que valor tiene {first_list[index]}? ")
#    second_list.append(value_for_key)
#    two_list_dictionary[first_list[index]]=second_list[index] ///Con esta linea me podría ahorrar el IF que sigue

#if (len(first_list) == len(second_list)): 
#    for position in range(0, len(first_list)):
#        two_list_dictionary[first_list[position]]=second_list[position]

#print(two_list_dictionary)




#Cree un programa que use una lista para eliminar keys de un diccionario.

important_dictionary = {}
delete_list = []

amount_values_dictionary = int(input("Cuantos datos quiere agregar al diccionario? "))

for index in range (0,amount_values_dictionary):
    new_key = input("Cual es el dato a guardar? ")
    value_for_key = input(f"Que valor tiene {new_key}? ")
    important_dictionary[new_key] = value_for_key

print(f"Los valores son:\n{important_dictionary}")

amount_deleted_items = int(input("Cuantos datos desea eliminar del diccionario? "))
for values in range (0, amount_deleted_items):
    delete_item = input("Que dato desea eliminar? ")
    delete_list.append(delete_item)

print(f"Los datos por eliminar son\n{delete_list}")

for deleted in list(important_dictionary.keys()):
    if deleted in delete_list:
        value_deleted = important_dictionary.pop(deleted)
        print(f"Se elimino {deleted}")

print(f"La lista final es:\n{important_dictionary}")