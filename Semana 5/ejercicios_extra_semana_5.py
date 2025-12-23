#Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
# Pida al usuario una lista de números y otro número a buscar

#number_list = []
#repeated = 0
#Amount_of_numbers = int(input("Cuantos numeros va a tener la lista? "))

#for index in range (0, Amount_of_numbers):
#    next_number = int(input(f"Ingrese el numero {index+1}: "))
#    number_list.append(next_number)

#important_number = int(input("Que numero desea buscar de la lista? "))

#for position in range (0, len(number_list)):
#    if (number_list[position] == important_number): 
#        repeated += 1

#print(f"La lista es: {number_list}")
#print(f"El numero {important_number} aparece un total de {repeated} veces")



#1. **Cree un programa que verifique si todos los elementos de una lista son positivos**
#- Restricciones:
#    - No use funciones como `all()`

#number_list = []

#Amount_of_numbers = int(input("Cuantos numeros va a tener la lista? "))

#for index in range (0, Amount_of_numbers):
#    next_number = int(input(f"Ingrese el numero {index+1}: "))
#    number_list.append(next_number)

#for positive in range(0, len(number_list)):
#    if (number_list[positive] < 0):
#        print(f"El numero {number_list[positive]} no es positivo!")
#print(f"La lista es {number_list}")



#Cree un programa que muestre el valor más pequeño de una lista sin usar min()
#Use una variable para comparar uno a uno

#number_list = []
#length_list= int(input("Cuantos valores tiene la lista? "))
#for index in range (0, length_list):
#    new_number = int(input(f"Digite su numero {index+1}:"))
#    number_list.append(new_number)

#lowest = number_list[0]

#for index in range (0, len(number_list)):
#    if (lowest > number_list[index]):
#        lowest = number_list[index]
#print(f"Mi lista: {number_list}. El mas pequeño es {lowest}")





#Cree un programa que reciba una lista de números y calcule el promedio de los valores, 
# luego cree una nueva lista con solo los valores mayores al promedio

#my_number_list = []

#length_list = int(input("Cuantos valores tiene la lista? "))

#for index in range(0, length_list):
#    new_number= int(input(f"Ingrese el numero {index+1}: "))
#    my_number_list.append(new_number)

#all_numbers= 0
#above_average = []
#for sum in range(0,len(my_number_list)):
#    all_numbers += my_number_list[sum]
#    average = all_numbers/len(my_number_list)

#for above in range(0,len(my_number_list)):
#    if (my_number_list[above] > average):
#        above_average.append(my_number_list[above])


#print (f"La lista es:\n{my_number_list}.\nEl promedio es de {average}, la nueva lista es la siguiente: \n{above_average}.")





#Cree un programa que le pida al usuario ingresar 5 palabras. 
# Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

word_list = []
more_than_4_list = []

for index in range(0,5):
    new_word = input("Ingrese una palabra: ")
    word_list.append(new_word)

for letters in range(0,5): 
    if (len(word_list[letters]) > 4):
        more_than_4_list.append(word_list[letters])

print(f"La lista original es {word_list}")
print(f"La lista con palabras de mas de 4 letras es {more_than_4_list}")