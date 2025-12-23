#1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#    1. Ejemplos:
#    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
#    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
#    Hay casos
#    en los
#    que la
#    iteracion por
#    indice es
#    muy util

#first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
#second_list = ['casos','los', 'la', 'por', 'es', 'util']


#for index in range(0,len(first_list)) and range(0,len(second_list)):
#    print(first_list[index], second_list[index])




#2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#    1. Pista: investigue de que otras maneras se puede usar el `range`.
#    2. Ejemplos:
#    3. `my_string = ‘Pizza con piña’`

my_string = input("Que desea ordenar? ")

for index in range(len(my_string), 0, -1):
    print(my_string[index-1])




#3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
#1. Ejemplos:
#    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`


#my_new_list = []
#amount_of_list_members = int(input("Cuantos integrantes va a agregar a la lista: "))

#for index in range(0,amount_of_list_members):
#	new_person = input("Nombre de la persona que desea agregar: ")
#	my_new_list.append(new_person)
#first_person = my_new_list[0]
#last_person = my_new_list[amount_of_list_members-1]

#print(my_new_list)
#print(f"first person: {first_person}")
#print(f"last person: {last_person}")

#my_new_list.pop(0)
#my_new_list.insert(0,last_person)
#my_new_list.pop(amount_of_list_members-1)
#my_new_list.append(first_person)
#print(my_new_list)




#4. Cree un programa que elimine todos los números impares de una lista.
#    1. Ejemplos:
#    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

#number_list = []
#pair_list = []

#amount_of_list_members = int(input("Cuantos numeros va a tener la lista: "))

#for index in range(0,amount_of_list_members):
#    new_number = int(input(f"Digite el numero de la posicion {index+1}: "))
#    number_list.append(new_number)

#for variable in range(0, len(number_list)):
#    if (variable < len(number_list)):
#        if(number_list[variable]%2 == 0):
#            pair_list.append(number_list[variable])

#print(f"La lista original es: {number_list}")
#print(f"La lista de pares es: {pair_list}")





#5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#    1. Ejemplos:
#    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

#number_list = []
#highest = 0
#for index in range (0, 10):
#    new_number = int(input(f"Digite su numero {index+1}:"))
#    number_list.append(new_number)
#    if (highest < new_number):
#        highest = new_number
#print(f"Mi lista: {number_list}. El mas alto es {highest}")