#Cree una calculadora por linea de comando. 
# Esta debe de tener un número actual, 
# y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, 
# el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
# El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, 
# o si ingresa un número invalido a la hora de hacer la operación.

def sum(first, second):
    total = first + second
    return total


def subtract(first, second):
    total = first - second
    return total


def multiply(first, second):
    total = first * second
    return total


def divide(first, second):
    total = first / second
    return total


def calculator():
    actual_number = 0
    answer_to_int = 0
    while (answer_to_int != 6):
        answer = input("Hola, Bienvenido a la calculadora de Mynor! Que desea hacer? \n1- Sumar  2- Restar  3- Multiplicar  4- Dividir  5- Limpiar Resultado  6- Salir \n: ")
        print(f"El numero actual es {actual_number}")        
        try: 
            answer_to_int = int(answer)
            if (answer_to_int == 1):
                second_number = input("Que numero desea sumar? ")
                second_to_int = float(second_number)
                result = sum(actual_number, second_to_int)
                print(f"El resultado de la suma es: {result}")
                actual_number = result
            elif (answer_to_int == 2):
                second_number = input("Que numero desea restar? ")
                second_to_int = float(second_number)
                result = subtract(actual_number, second_to_int)
                print(f"El resultado de la resta es: {result}")
                actual_number = result
            elif (answer_to_int == 3):
                second_number = input("Que numero desea multiplicar? ")
                second_to_int = float(second_number)
                result = multiply(actual_number, second_to_int)
                print(f"El resultado de la multiplication es: {result}")
                actual_number = result
            elif (answer_to_int == 4):
                second_number = input("Que numero desea dividir? ")
                second_to_int = float(second_number)
                result = divide(actual_number, second_to_int)
                print(f"El resultado de la division es: {result}")
                actual_number = result
            elif (answer_to_int == 5):
                actual_number = 0
                print(f"se limpio el resultado! \n{actual_number}")
            if (answer_to_int > 6 or answer_to_int < 1): 
                raise IndexError()
            # if (answer_to_int.isalpha()): 
            #     raise ValueError()
        except IndexError:
            print("El numero ingresado no es una opción!")
        except ValueError:
            print("El ejercicio solo acepta números enteros entre las opciones, no decimales ni letras!")
    else: 
        print("Hasta luego, nos vemos pronto!")


def main():
    try:
        calculator()
    except Exception as ex:
        print(f"Ha ocurrido un error inesperado: {ex}")

main()