#1. Cree un programa que:
#- Pida al usuario su **nombre**
#    Si el nombre es numérico (`isdigit()`), **haga `raise ValueError("El nombre no puede ser un número")`**
#- Luego pida su edad
#   Si no es un número válido, capture el `ValueError` y muestre un mensaje
#Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"


# def validate_name(name):
#     try:
#         if (name.isdigit()):
#             raise ValueError()
#         else:
#             return name
#     except ValueError:
#         print("El nombre no puede ser un número!")


# def validate_age(user_age):
#     try:
#         final_age=int(user_age)
#         if (final_age > 0 and final_age < 110):
#             return final_age
#         else:
#             raise ValueError("Edad fuera del rango o no numeral!")
#     except ValueError as exception:
#         print(f"Se produjo un error: {exception}")

# def ask_all_info():
#         final_age = 0
#         try:
#             name = input("Digite su nombre: ")
#             if (name.isdigit()):
#                 raise ValueError("El nombre no puede ser un número")
#             user_age = input("Ahora digite su edad: ")
#             if (user_age.isdigit()):
#                 final_age=int(user_age)
#                 if (final_age > 0 and final_age < 110):
#                     print(f"Hola {name}, su edad es {final_age}")
#                 else:
#                 #print("si entra")
#                     wrong_age=ValueError("La edad no es un numero valido!")
#                     raise ValueError(wrong_age)
#             else:
#                 raise ValueError("La edad tiene que ser un numero entero y positivo!")
#         except ValueError as error:
#                 print(error)


# def main(): 
#     try: 
#         ask_all_info()
#     except Exception as detail:
#         print(f"Se produjo el siguiente error: {detail}")


# main()


# def create_list():
#     data_list = []
#     amount_of_values = int(input("Cuantos datos desea ingresar en la lista: "))
#     for validation in range(0, amount_of_values):
#         new_value = input("Que dato desea agregar? ")
#         data_list.append(new_value)
#     return data_list


# def convert_to_int(list):
#     for value in list:
#         try:
#             final_value = int(value)
#             print(f"El valor {value} se convirtió correctamente a {final_value}")
#         except ValueError as error:
#             print(f"No se pudo convertir el valor {value}, Error: {error}")


# def main():
#     try:
#         important_list = create_list()
#         convert_to_int(important_list)
#     except Exception as final_exception:
#         print(f"Hubo un error en el sistema: {final_exception}")


# main()


def create_list():
    my_list = []
    elements = int(input("Cuantos elementos desea agregar a la lista: "))
    for amount in range(0,elements):
        new_value = input("Cual valor desea agregar: ")
        my_list.append(new_value)
    return my_list


def sum_values(the_list):
    total = 0
    for value in the_list:
        try:
            converted = float(value)
            total += converted
            print(f"El valor {converted} se ha sumado correctamente")
        except ValueError:
            print(f"Elemento invalido: {value}")
    print(f"Total de la suma: {total}")


def main():
    try:
        new_list = create_list()
        sum_values(new_list)
    except Exception as exc: 
        print(f"Ha ocurrido un error inesperado: {exc}")


main()