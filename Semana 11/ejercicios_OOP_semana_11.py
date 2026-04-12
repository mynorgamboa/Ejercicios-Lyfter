class Circle:
    def __init__(self, rad):
        self.radius = rad

    def get_area(self):    
        area = 3.1415926536 * (self.radius ** 2)
        print(f"El area del circulo es {area}")
        return area

my_circle = Circle(20)
my_circle.get_area()


class Person:
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0

class Bus:

    def __init__(self, max_pass):
        self.max_passengers = max_pass
        self.amount_passengers = 0
        self.passengers = []

    def get_on_the_bus(self, new_passenger):
        all_passengers = []
        if (self.amount_passengers <= self.max_passengers):
            self.passengers.append(new_passenger)
            self.amount_passengers += 1
            for passenger in self.passengers:
                all_passengers.append(passenger.name)
            print(f'Los pasajeros son: {all_passengers}')
        else:
            print("El bus esta al máximo, ya nadie puede subir!")
    
    
    def get_off_the_bus(self):
        if self.passengers:
            all_passengers = []
            last = self.passengers.pop()
            self.amount_passengers -= 1
            for passenger in self.passengers:
                all_passengers.append(passenger.name)
            print(f"Se bajó a {last.name} y quedan los siguientes: {all_passengers}")
        else:
            print('El Bus esta vacío!')

my_bus = Bus(5)
my_bus.amount_passengers = 1

name = input("Cual es el nombre del siguiente pasajero? ")
person_1 = Person(name)
my_bus.get_on_the_bus(person_1)

name_2 = input("Cual es el nombre del siguiente pasajero? ")
person_2 = Person(name_2)
my_bus.get_on_the_bus(person_2)

name_3 = input("Cual es el nombre del siguiente pasajero? ")
person_3 = Person(name_3)
my_bus.get_on_the_bus(person_3)

name_4 = input("Cual es el nombre del siguiente pasajero? ")
person_4 = Person(name_4)
my_bus.get_on_the_bus(person_4)

name_5 = input("Cual es el nombre del siguiente pasajero? ")
person_5 = Person(name_5)
my_bus.get_on_the_bus(person_5)

name_6 = input("Cual es el nombre del siguiente pasajero? ")
person_6 = Person(name_6)
my_bus.get_on_the_bus(person_6)

my_bus.get_off_the_bus()
my_bus.get_off_the_bus()
my_bus.get_off_the_bus()
my_bus.get_off_the_bus()
my_bus.get_off_the_bus()
my_bus.get_off_the_bus()


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet):
        self.feet = feet


head = Head()
right_hand = Hand()
left_hand = Hand()
left_feet = Feet()
right_feet = Feet()
left_arm = Arm(left_hand)
right_arm = Arm(right_hand)
left_leg = Leg(left_feet)
right_leg = Leg(right_feet)

torso = Torso(head,right_arm, left_arm, right_leg, left_leg)

class Human:
    def __init__(self,torso, name):
        self.torso = torso
        self.name = name
        print(f'{name} has Born! Congratulations!')

new_name = input('What is the human name? ')
new_human = Human(torso,new_name)