#1. Dada una lista de ventas con la siguiente información:
#    - `date`
#    - `customer_email`
#    - `items`
#- Y cada item teniendo la siguiente información:
#    - `name`
#    - `upc`
#    - `unit_price`
#- Cree un diccionario que guarde el total de ventas de cada UPC.

# print("Posibles UPCs: Computadora: 101, Televisor: 102, radio: 103, Teléfono: 104")

# total_list = []
# total_sales = {}

# tv_total = 0
# cellphone_total = 0
# pc_total = 0
# radio_total = 0

# amount_of_sales = int(input("Cuantas ventas desea ingresar? "))

# for sales in (0, amount_of_sales-1):

#     all_the_sales = {}
#     sales_list = []
#     date = input("Cual es la fecha de la venta? ")
#     customer_email = (input("Cual es el correo electrónico? "))
#     items = int(input("Cuantos items se vendieron? "))

#     all_the_sales["date"] = date
#     all_the_sales["customer_email"] = customer_email

#     for index in range(0, items):
#         items_dictionary = {}
#         name = input("Cual es el nombre del item? ")
#         upc = input("Cual es el UPC del item? ")
#         unit_price = float(input("Cual es el precio por unidad? "))

#         items_dictionary["name"] = name
#         items_dictionary["upc"] = upc
#         items_dictionary["unit_price"] = unit_price

#         sales_list.append(items_dictionary)

#     all_the_sales["items"] = sales_list

#     total_list.append(all_the_sales)

# for position in range(0, len(total_list)):
#     print(f"La venta {position+1} es la siguiente: \n{total_list[position]}")


# for position in total_list:
#     for item in position["items"]:
#         upc = item["upc"]
#         price = float(item["unit_price"])
#         if (upc not in total_sales):
#             total_sales[upc] = 0
        
#         total_sales[upc] += price
# print(total_sales)

# crear dict total_sales = {}
# por cada venta en total_list:
#     por cada item en venta["items"]:
#         upc = item["upc"]
#         precio = item["unit_price"]
#         si upc no está en total_sales:
#             total_sales[upc] = 0
#         total_sales[upc] += precio
# imprimir total_sales


#1. Agrupar empleados por departamento
#- Dada una lista de empleados donde cada uno tiene nombre, 
#correo y departamento, cree un diccionario que agrupe los 
#empleados por su departamento:

total_of_employees = []
amount_of_employees = int(input("Cuantos empleados desea ingresar? "))

for employees in range (0, amount_of_employees): 
    all_the_employees = {}
    name = input("Cual es el nombre del empleado? ")
    email = input("Cual es el correo electrónico? ")
    department = input("Cual es el departamento del empleado? ")

    all_the_employees["name"] = name
    all_the_employees["email"] = email
    all_the_employees["department"] = department

    total_of_employees.append(all_the_employees)

#print(total_of_employees)

all_the_groups = {}

for order in total_of_employees:
    dept = order["department"].lower()
    if (dept not in all_the_groups):
        all_the_groups[dept] = []
    all_the_groups[dept].append(order)
#print (all_the_groups)

for each_dept  in all_the_groups:
    print (f"Los empleados por departamentos son: \n{each_dept}: {all_the_groups[each_dept]}")

# grouped = {}
# por cada empleado en total_of_employees:
#     dept = normalizar(empleado["department"])
#     si dept no está en grouped:
#         grouped[dept] = []
#     grouped[dept].append(empleado)
# imprimir grouped