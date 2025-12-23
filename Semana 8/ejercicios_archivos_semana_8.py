# Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_order_and_print_file_per_line(path):
	new_list = []
	try:
		with open(path) as file:
			for line in file.readlines():
				new_list.append(line)
				#print(f"Linea guardada: {line}")
			print(f"La lista es: {new_list}")
			new_list.sort()
			print(f"La lista organizada es: {new_list}")
		return new_list
	except Exception as error:
		print(f'Ha ocurrido un error en "open_order_and_print_file_per_line()": {error}')


def create_new_document(the_answer,the_list):
	try:
		with open(the_answer, 'w') as file:
			for index in the_list:
				file.writelines(f"{index}")
				print(f"Se guardo correctamente la posición {index}")
	except Exception as error:
		print(f'Ha ocurrido un error en "create_new_document()": {error}')

def main():
	try:
		get_the_list = open_order_and_print_file_per_line('hello.txt')
		create_new_document('ordered_list.txt', get_the_list)
	except Exception as error:
		print(f"Ha ocurrido un error inesperado: {error}")


main()