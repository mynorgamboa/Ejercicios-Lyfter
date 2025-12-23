#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

# def print_first_message ():
#     print("Necesitamos apoyo!!!!!")
#     show_second_message()


# def show_second_message():
#     print("Ya acaba de llegar el apoyo!! ")


# def main():
#     print_first_message()

# main()

# 2. Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.
#     2.  Intente accesar a una variable global desde una función y cambiar su valor.

# global_message = "This message is from outside the planet earth!"


# def get_global_message():
#     global global_message
#     global_message = "This is from Costa Rica, the best country in the world!"
#     print(global_message)


# def main():
#     print(global_message)
#     get_global_message()

# main()


# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

# new_list = []

# def create_new_list ():
#     amount_of_values = int(input("Cuantos datos va a tener la lista? ")) 

#     for values in range(0, amount_of_values):
#         new_value = int(input("Cual es el dato a guardar? "))
#         new_list.append(new_value)
#     return new_list


# def sum_all_values(the_list):
    
#     total = 0

#     for each in the_list:
#         total += each
#     return total


# def print_total():
#     print(f"El total de sumar todos los números es: \n{sum_all_values(new_list)}")


# def main():
#     create_new_list()
#     print_total()


# main()


# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

# new_string = input("Cual es el String que desea agregar? ")

# def turn_around_the_string(the_string):
#     for index in range(len(the_string), 0, -1):
#         print(the_string[index-1])
#     return index


# def main():
#     turn_around_the_string(new_string)


# main()



# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

# new_string = input("Cual es el String que desea agregar? ")


# def verify_if_upper_or_lower(the_string):
#     uppers = 0
#     lowers = 0
#     lower_accent = ["á","é","í","ó","ú"]
#     upper_accent = ['Á', 'É', 'Í', 'Ó', 'Ú']
#     for value in the_string:
#         if (value >= "A" and value <= "Z" or (value in upper_accent)):
#             uppers += 1
#         elif(value >= "a" and value <= "z" or (value in lower_accent)): 
#             lowers += 1
#     print (f"El string {the_string} tiene {uppers} mayúsculas y {lowers} minúsculas")


# def main():
#     verify_if_upper_or_lower(new_string)


# main()


# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

# new_string = input("Digite el string separado de guiones (Ej: python-variable-funcion-computadora-monitor): ")

# def order_the_string(the_string):
#     new_list = []
#     new_word=""
#     for index in range(0,len(the_string)):
#         if (the_string[index] != "-"):
#             new_word=new_word+the_string[index]
#         else:
#             new_list. append(new_word)
#             new_word=""
#     new_list.append(new_word)
#     new_word=""
#     print(f"la lista desorganizada es {new_list}")
#     new_list.sort()
#     print(f"la lista organizada es {new_list}")
    
#     for position in new_list:
#         new_word = new_word+position
#         new_word = new_word+"-"
#     new_word = new_word[:-1]

#     print(f"El string final es: {new_word}")


# def main():
#     order_the_string(new_string)


# main().

#7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo,
#y conviertala a codigo. No busque el codigo, eso no ayudaria.



def create_square_list(number):
    square_root = number**0.5
    prime_list=[]
    for index in range (0, int(square_root)):
        prime_list.append(index+1)
    return prime_list

def create_list():
    new_list = []
    amount_of_values = int(input("Cuantos datos va a tener la lista? "))
    for index in range(0, amount_of_values):
        new_value = int(input(f"Cual es el valor {index+1} a agregar? "))
        new_list.append(new_value)
    return new_list


def verify_if_prime():
    final_list = []
    divisibles = 0
    list_to_validate = create_list()
    for value in list_to_validate:
        if(value == 2):
            final_list.append(value)
        elif(value > 2):
            for div in create_square_list(value):
                #print(f"Lista de numeros menores a la raiz cuadrada de {value}: \n {create_square_list(value)}") 
                if (value % div == 0):
                    divisibles += 1
                    #print(f"Para el numero {value} hay {divisibles} divisibles")
            if (divisibles < 2):
                final_list.append(value)
            divisibles=0
    return final_list


def main():
    print(f"La lista de primos es: \n{verify_if_prime()}")


main()