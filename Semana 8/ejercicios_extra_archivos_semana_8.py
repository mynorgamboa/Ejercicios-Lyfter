# Cree un programa que lea un archivo con texto línea por línea, 
# quite los saltos de línea (\n) 
# y escriba todo el contenido en un solo renglón en un nuevo archivo

# def read_and_save_line_per_line(path):
#     new_list = []
#     str = ""
#     try:
#         with open(path) as file:
#             for line in file.readlines():
#                 for index in line:
#                     if (index != "\n"):
#                         #print(f"index:{index}")
#                         str = str + index
#                         #print(f"str: {str}")
#                     else:
#                         new_list.append(str)
#                         str = ""
#             return new_list
#     except Exception as error:
#         print(f'Hubo un error en read_and_save_line_per_line(): {error}')


# def create_only_one_line(list_created, document):
#     one_line = ""
#     try:
#         for index in list_created:
#             one_line = one_line + index + " "
#         print(f'Linea completa: {one_line}')
#         with open(document, 'w') as file:
#             file.write(one_line)
#     except Exception as error:
#         print(f'Hubo un error en create_only_one_line: {error}')


# def main():
#     try:
#         path = read_and_save_line_per_line('important_text.txt')
#         create_only_one_line(path, 'exercise_1.txt')
#     except Exception as error:
#         print(f'Hubo un error inesperado: {error}')


# main()


# 1. Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o saltos de línea)

# def open_and_count_words(path):
#     count = 1
#     try:
#         with open(path, encoding='utf-8') as file: 
#             for index in file: 
#                 print (index)
#                 for words in index:
#                     if(words == " " or words == "\n"):
#                         count += 1
#         print (f'Las palabras son: {count}')
#     except Exception as error: 
#         print(f'Ha ocurrido un error en open_and_count_words(): {error}')


# def main():
#     try:
#         open_and_count_words('important_text.txt')
#     except Exception as error: 
#         print(f'Ha ocurrido un error inesperado: {error}')


# main()


# 1. Cree un programa que:
# - Lea un archivo línea por línea
# - Convierta cada línea a **mayúsculas**
# - Escriba el contenido en un **nuevo archivo**

# def read_and_capital(path):
#     try:
#         str = ""
#         with open(path) as file: 
#             for line in file.readlines():
#                 str += line.upper()
#             return str
#     except Exception as error: 
#         print(f'Ha ocurrido un error en read_and_capital(): {error}')


# def create_new_file(capitalized, new_file):
#     try:
#         with open(new_file, 'w', encoding='UTF-8') as file:
#             file.write(capitalized)
#         with open(new_file) as readable: 
#             print(readable.read())
#     except Exception as error:
#         print(f'Ha ocurrido un error en create_new_file(): {error}')


# def main():
#     try:
#         capitalized = read_and_capital('lower_text.txt')
#         create_new_file(capitalized, 'upper_text.txt')
#     except Exception as error: 
#         print(f'Ha ocurrido un error inesperado: {error}')

# main()


# 1. Cree un programa que:
# - Pida al usuario una línea de texto
# - Agregue esa línea **al final** de un archivo existente
# - Si el archivo no existe, lo crea automáticamente


def get_text_line():
    try:
        text_line = input('Ingrese una linea de texto que desee agregar al documento: ')
        text_line += '\n'
        return text_line
    except Exception as error:
        print(f'Hubo un error en get_text_line(): {error}')


def add_text_line(text_line):
    try:
        with open('final_document.txt', 'a') as file: 
            file.write(text_line)
        print('El proceso ha finalizado y el documento fue creado o la linea fue agregada!')
    except Exception as error:
        print(f'Hubo un error en add_text_line(): {error}')


def main():
    try:
        line_from_user = get_text_line()
        add_text_line(line_from_user)
    except Exception as error:
        print(f'Hubo un error inesperado: {error}')

main()