
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def get_area(rectangle):
        area = rectangle.width * rectangle.height
        if (rectangle.width > 0 and rectangle.height > 0):
            print(f'The area of the rectangle is {area}')
        else:
            print('There is a negative value, try again!')

    def get_perimeter(rectangle):
        perimeter = 2 * (rectangle.width+rectangle.height)
        if (rectangle.width > 0 and rectangle.height > 0):
            print(f'The perimeter of the rectangle is {perimeter}')
        else:
            print('There is a negative value, try again!')
        

width = int(input('What is the width? '))
height = int(input('What is the height? '))

new_rectangle = Rectangle(width,height)
new_rectangle.get_area()
new_rectangle.get_perimeter()



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def acceleration(self, amount):
        self.speed += amount
    
    def brake(self, amount):
        self.speed -= amount
    
    def __str__(self):
        print(f'{self.brand} {self.model} --> {self.speed} km/h')

brand = input('What is the car brand? ')
model = input(f'What is the {brand} model? ')
new_car = Car(brand, model)

acceleration = int(input('What is the acceleration? '))
new_car.acceleration(acceleration)
new_car.__str__()

brake = int(input('What is the brake? '))
new_car.brake(brake)
new_car.__str__()