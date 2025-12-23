#Dadas las horas trabajadas de una persona y su tarifa por hora, calcular y mostrar su salario.

worked_hours=int(input("Ingrese sus horas trabajadas: "))
pay_per_hour=int(input("Cual es su salario por hora: "))
salary=worked_hours*pay_per_hour
print(f"Su salario es de {salary}")



username=input("Ingrese su nombre: ")
lastname=input("Ingrese su apellido:")
email_domain=input("Ingrese el nombre de su empresa: ")
print(f"Su email es {username}.{lastname}@{email_domain}.com")


#Dado el nombre y apellido de un empleado, y el dominio .com de una empresa,
#genere su email usando el formato <nombre>.<apellido>@<dominio_de_empresa>.com.