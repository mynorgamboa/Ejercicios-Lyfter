
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def get_area(rectangle):
        try:
            area = rectangle.width * rectangle.height
            if (rectangle.width > 0 and rectangle.height > 0):
                return area
            else:
                raise ValueError()
        except ValueError as ex:
            print('There is a negative value, try again!')

    def get_perimeter(rectangle):
        try:
            perimeter = 2 * (rectangle.width+rectangle.height)
            if (rectangle.width > 0 and rectangle.height > 0):
                return perimeter
            else:
                raise ValueError()
        except ValueError as ex:
            print('There is a negative value, try again!')
            
width = int(input('What is the width? '))
height = int(input('What is the height? '))

new_rectangle = Rectangle(width,height)
print(f'The area of the rectangle is {new_rectangle.get_area()}')
print(f'The perimeter of the rectangle is {new_rectangle.get_perimeter()}')


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Hace un sonido'


class Dog(Animal):
    def speak(self):
        return 'Guau'

class Cat(Animal):
    def speak(self):
        return 'Miau'


my_dog = Dog('Ellie')
my_cat = Cat('Gigi')

print(f'Mi perro se llama {my_dog.name} y hace {my_dog.speak()}')
print(f'Mi gato se llama {my_cat.name} y hace {my_cat.speak()}')


#Cree una clase Product con: Nombre, precio y cantidad
#Cree una clase Inventory que: Guarde productos en una lista
#Tenga métodos para: Agregar un producto, Mostrar todos los productos, Calcular el valor total del inventario

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self. quantity = quantity


class Inventory:
    def __init__(self):
        self.product_lists = []

    
    def add_product(self, product):
        self.product_lists.append(product)
        return self.product_lists

    def show_products(self):
        print ('Los productos son: ')
        for product in self.product_lists:
            print(f'Nombre: {product.name}, Precio: {product.price}, Cantidad: {product.price}')

    def total_amount(self):
        total_price = 0
        for product in self.product_lists:
            total_unit = (product.quantity * product.price)
            total_price += total_unit
        return total_price

product_1 = Product("PS5",250000,7)
product_2 = Product("PC gamer", 350000,2)
product_3 = Product("Switch 2", 200000, 5)

inventory = Inventory()

inventory.add_product(product_1)
inventory.add_product(product_2)
inventory.add_product(product_3)

inventory.show_products()

print(f'El precio total de todo es: {inventory.total_amount()}')