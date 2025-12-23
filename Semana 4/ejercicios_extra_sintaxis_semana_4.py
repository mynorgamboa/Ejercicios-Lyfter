#1. Pasa los @Ejercicios de Pseudocódigo previamente creados a código
#    a. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
#        i. Si el precio es menor a 100, el descuento es del 2%.
#        ii. Si el precio es mayor o igual a 100, el descuento es del 10%.
#        iii. *Ejemplos*:
#            1. 120 → 108
#            2. 40 → 39.2

#product_price = int(input("Digite el precio del producto: "))

#if (product_price < 100): 
#    price_with_discount = product_price - product_price*0.02
#else: 
#    price_with_discount = product_price - product_price*0.10
#print(f"El precio final del producto es de: {price_with_discount}")



#2. Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es menor o mayor a 10 minutos. 
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”.
#  Si es exactamente igual, muestre “*Igual*”.
#    1. *Ejemplos*:
#        1. 1040 → Mayor
#        2. 140 → 460
#        3. 600 → Igual
#        4. 599 → 1

#seconds= int(input("Digite el tiempo en segundos: "))

#if (seconds < 600): 
#    print(f"Hacen falta {600-seconds} segundos")
#elif (seconds == 600):
#    print("Igual a 10 minutos")
#else: 
#    print("Es Mayor a 10 minutos")



#3. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado.
# Luego muestre el resultado de la suma.
#    1. 5 → 15 (1 + 2 + 3 + 4 + 5)
#    2. 3 → 6 (1 + 2 + 3)
#    3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

#user_number = int(input("Ingrese su numero: "))
#counter = 0
#total = 0

#while (counter < user_number):
#    counter += 1 
#    total += counter
#print(f"El total es {total}")

#1. Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (`primero` y `segundo`)
#  y los ordene de menor a mayor en dichas variables.
#    1. Ejemplos:
#        1. A: 56, B: 32 → A: 32, B: 56
#        2. A: 24, B: 76 → A: 24, B: 76
#        3. A: 45, B: 12 → A: 12, B: 45

#first = int(input("Digite su primer numero: "))
#second = int(input("Digite su segundo numero: "))

#if (first < second): 
#    print(f"A: {first}, B: {second}")
#else: 
#    third = first
#    first = second
#    print(f"A: {first}, B: {third}")




#2. Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. 
# Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.
#    1. *Ejemplos*:
#        1. 73 → 20.27
#        2. 50 → 13.88
#        3. 120 → 33.33

#speed = int(input("Digite la velocidad en km/h: "))

#ms_speed= speed*1000/3600
#print(f"Su velocidad en m/s es de {ms_speed}")




#3. Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, 
# ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
#    1. *Ejemplos*:
#        1. 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
#        2. 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
#        3. 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres

#counter = 0
#men_amount = 0
#women_amount = 0

#while (counter<6):
#    counter += 1
#    sex=int(input("Cual es el sexo de la persona. Digite 1 si es mujer, 2 si es hombre: "))
#    if (sex == 1):
#        women_amount += 1
#    else: 
#        men_amount += 1
#men_average = men_amount / 6 * 100
#women_average = women_amount / 6 * 100

#print(f"Promedio de hombres: {men_average}%")
#print(f"Promedio de mujeres: {women_average}%")





#3. Cree un diagrama de flujo que pida 3 números al usuario. 
# Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “*Correcto*”. Sino, mostrar “*incorrecto*”.
#    1. *Ejemplos*:
#        1. 23, 30, 768 → Correcto (hay un 30)
#        2. 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#        3. 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)


#first = int(input("Digite el primer numero: "))
#second = int(input("Digite el segundo numero: "))
#third = int(input("Digite el tercer numero: "))

#if (first==30 or second==30 or third==30 or first+second+third==30):
#    print("Correcto!")
#else: 
#    print("Incorrecto!")



#1. Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.
#    1. *Ejemplos*:
#        1. 4, 76, 43, 6, 8 → 76
#        2. 1, 2, 3, 6, 7 → 7
#        3. 2132, 4355, 1132, 2323, 1214 → 4355

#counter = 0
#first = int(input("Digite el primer numero: "))
#while (counter<4):
#    counter += 1
#    second = int(input("Digite el siguiente numero: "))
#    if (first < second):
#        first = second
#        highest = second
#    else: 
#        highest = first
#print(f"El numero mayor es: {highest}")




#2. Cree un diagrama de flujo que le pida un numero al usuario 
# y muestre “*Fizz*” si es divisible entre 3, “*Buzz*” si es divisible entre 5, y “*FizzBuzz*” si es divisible entre ambos.
#    1. *Ejemplos*:
#        1. 33 → Fizz
#        2. 25 → Buzz
#        3. 30 → FizzBuzz

#user_number = int(input("Digite el numero a calcular: "))

#if (user_number%3 == 0 and user_number%5 == 0):
#    print("FizzBuzz")
#elif (user_number%3 ==0):
#    print("Fizz")
#elif(user_number%5 == 0): 
#    print("Buzz")




#Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.

#total = 0
#counter = 0

#while (counter < 100): 
#    counter += 1
#    current_number = int(input("Digite el numero que desea guardar: "))
#    total += current_number
#print(f"El total es de: {total}")





#3. **Convertidor de unidades de temperatura**
#    - Pida al usuario ingresar una temperatura en Celsius
#    - Conviértala a Fahrenheit y Kelvin
#    - Muestre los tres valores

#temperature = int(input("Proporcione la temperatura en grados Celsius: "))

#fahrenheit = (temperature* 1.8)+32
#kelvin = temperature + 273.15

#print(f"Grados Celsius: {temperature}")
#print(f"Grados Fahrenheit: {fahrenheit}")
#print(f"Grados Kelvin: {kelvin}")





#4. **Tabla de multiplicar personalizada**
#    - Pida al usuario un número del 1 al 10
#    - Muestre su tabla de multiplicar del 1 al 12

number = int(input("Digite un numero del 1 al 10 para la tabla: "))

my_first_list = [number*1, number*2, number*3,number*4, number*5, number*6,
                 number*7, number*8, number*9, number*10,number*11, number*12]

counter = 0
while(counter < 12):
    counter +=1
    print(f"{number} * {counter} = {my_first_list[counter-1]}")