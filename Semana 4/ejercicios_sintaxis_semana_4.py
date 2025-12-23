#1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
 #a. Si le salen errores, **no se asuste.** Léalos e intente comprender qué significan.
  #Los errores son oportunidades de aprendizaje.
   #b.Por ejemplo:
        #1. string + string → ?
        #2. string + int → ?
        #3. int + string → ?
        #4. list + list → ?
        #5. string + list → ?
        #6. float + int → ?
        #7. bool + bool → ?

#print("texto1"+"texto2")

#print("texto1"+147)

#print(355+"texto1")

#first_list = [1,45,77,99]
#second_list = [12,13]
#print(first_list+second_list)

#first_list = [1,45,77,99]
#print("Esta es mi primer lista: "+first_list)

#print(15.15+35)

#print(True+True)



#2. Cree un programa que le pida al usuario su nombre, apellido, y edad,
#y muestre si es un bebé, niño, preadolescente, adolescente,
#adulto joven, adulto, o adulto mayor.

#user_name = input("Digite su nombre: ")
#last_name = input("Digite su apellido: ")
#user_age = int(input("Digite su edad: "))

#if (user_age < 5):
#    print(f"{user_name} {last_name},Eres un bebe!")
#elif (user_age < 12):
#    print(f"{user_name} {last_name},Eres un preadolescente!")
#elif (user_age < 18):
#    print(f"{user_name} {last_name},Eres un adolescente!")
#elif (user_age < 30):
#    print(f"{user_name} {last_name},Eres un adulto joven!")
#elif(user_age < 65):
#    print(f"{user_name} {last_name},Eres un adulto")
#else: 
#    print(f"{user_name} {last_name},Eres un adulto mayor!")




#3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#    a. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
#import random

#secret_number = random.randint(1,10)
#user_number = -1
#while (user_number != secret_number): 
#    user_number = int(input("Cual es el numero secreto: "))
#    if (user_number == secret_number):
#        print("Correcto!")
#    else:
#        print("Incorrecto!")



#4. Cree un programa que le pida tres números al usuario y muestre el mayor.

#first = int(input("Digite el primer numero: "))
#second = int(input("Digite el segundo numero: "))
#third = int(input("Digite el tercer numero: "))

#if (first > second): 
#    if(first > third): 
#        print(f"El numero mayor es {first}")
#elif(second > third): 
#    print(f"El numero mayor es {second}")
#else: 
#    print(f"El numero mayor es {third}")



#5. Dada `n` cantidad de notas de un estudiante, calcular:
#    1. Cuantas notas tiene aprobadas (mayor a 70).
#    2. Cuantas notas tiene desaprobadas (menor a 70).
#    3. El promedio de todas.
#    4. El promedio de las aprobadas.
#    5. El promedio de las desaprobadas.

grades_to_analyze = int(input("Ingrese la cantidad de notas que va a calcular: "))
grade_quantity = 0
approved_grades = 0
disapproved_grades = 0
sum_grades = 0
actual_grade = 0
sum_approved = 0
sum_disapproved = 0

while (grade_quantity < grades_to_analyze): 
    grade_quantity += 1
    actual_grade = float(input(f"Ingrese la nota numero {grade_quantity}: "))
    if (actual_grade >= 70):
        approved_grades += 1
        sum_grades += actual_grade
        sum_approved += actual_grade
    else:
        disapproved_grades += 1    
        sum_grades += actual_grade
        sum_disapproved += actual_grade
average = sum_grades/grades_to_analyze
if(sum_approved == 0):
    approved_average = 0
    print(f"Aprobadas: 0")
else: 
    approved_average = sum_approved / approved_grades
    print(f"Aprobadas: {approved_grades}, El Promedio es de {int(approved_average)}")
if(sum_disapproved == 0):
    disapproved_average = 0
    print(f"Aprobadas: 0")
else: 
    disapproved_average = sum_disapproved / disapproved_grades
    print(f"Desaprobadas: {disapproved_grades}, El Promedio es de {int(disapproved_average)}")
print(f"Promedio total: {int(average)}")