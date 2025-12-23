#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#    - `nombre`
#    - `numero_de_estrellas`
#    - `habitaciones`
#El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información: numero, piso, precio por noche

#Pistas para rehacer (sin código)
#• Dentro del for:
#    ◦ Crear habitación = {numero: …, piso: …, precio_por_noche: …}
#    ◦ Agregar habitación a habitaciones (lista)
#    • Al final: hotel = {nombre: …, numero_de_estrellas: …, habitaciones: […]}

hotel_dictionary = {}
rooms_list = []
hotel_name = input("Cual es el nombre del hotel? ")
stars_number = int(input("Cuantas estrellas tiene? "))
rooms = int(input("Cuantas habitaciones tiene? "))

hotel_dictionary["nombre"] = hotel_name
hotel_dictionary["numero_de_estrellas"] = stars_number

for index in range(0, rooms):
    room_dictionary = {}
    room_number = int(input(f"Cual es el numero del cuarto {index+1}? "))
    floor_number = int(input("Cual es el numero del piso? "))
    price_by_night = float(input("Cual es el precio por noche? "))

    room_dictionary["numero"] = room_number
    room_dictionary["piso"] = floor_number
    room_dictionary["precio_por_noche"] = price_by_night
#    print(room_dictionary)

    rooms_list.append(room_dictionary)

#    print(rooms_list)

hotel_dictionary[f"habitaciones"] = rooms_list

print(hotel_dictionary)