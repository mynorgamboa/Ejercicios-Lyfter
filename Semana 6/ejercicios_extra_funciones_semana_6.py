#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto


# def how_many_times (text, letter):
#     text=text.lower()
#     counter = 0
#     for index in text:
#         if (index == letter): 
#             counter += 1
#     print(f"La letra {letter} aparece {counter} veces")


# def main():
#     full_string = input("Cual es el texto a ingresar? ")
#     important_letter = input("Cual es la letra a buscar en el texto? ")
#     how_many_times(full_string, important_letter)


# main()


#Cree una función que reciba una lista de palabras y un número n,
# y retorne una nueva lista con solo las palabras que tengan más de n letras

# def more_than_amount(list, letters):
#     new_list = []
#     for index in list:
#         if (len(index) > letters):
#             new_list.append(index)
#     return new_list


# def create_list():
#     words_list = []
#     amount_words = int(input("Cuantas palabras va a tener la lista? "))
#     for index in range(0,amount_words):
#         word = input("Que palabra desea agregar a la lista? ")
#         words_list.append(word)
#     print(f"Esta es la lista original: \n{words_list}")
#     return words_list


# def main():
#     full_list = create_list()
#     word_length = int(input("Cuantas letras es el mínimo de las palabras a mostrar? "))
#     result = more_than_amount(full_list, word_length)
#     print(f"Las palabras con mas de {word_length} letras son: \n{result}")


# main()


#Cree una función que reciba un string y retorne cuántas vocales contiene

def count_the_string(text):
    comparison = ["a","e","i","o","u","á","é","í","ó","ú"]
    text = text.lower()
    counter = 0
    for index in text:
        if index in comparison:
            counter += 1
    return counter


def main():
    the_string = input("Cual es el texto para analizar? ")
    final_answer = count_the_string(the_string)
    print(f"Hay {final_answer} vocales en el texto. ")


main()