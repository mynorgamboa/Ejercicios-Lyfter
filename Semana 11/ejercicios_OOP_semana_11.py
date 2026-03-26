class Circle:
    def get_area(self, radius):    
        self.radius = radius
        area = 3.1415926536 * (self.radius ** 2)
        print(f"El area del circulo es {area}")

my_circle = Circle()
my_circle.get_area(4)


class Person:
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0


class Bus:
    max_passengers = 5
    passengers = []
    amount_passengers = 1

    def get_on_the_bus(self):
        
        while (self.amount_passengers <= self.max_passengers):
            named = input("Cual es el nombre del pasajero? ")
            new_passenger = Person(named)
            self.passengers.append(new_passenger.name)
            self.amount_passengers += 1
            print(self.passengers)
        else:
            print("El bus esta al máximo!")
    
    
    def get_off_the_bus(self):

        while (len(self.passengers) >= 1):
            last = self.passengers.pop()
            self.amount_passengers -= 1
            print(f"Se bajó a {last} y quedan los siguientes: {self.passengers}")
        else:
            print("El bus esta vacío!")

my_bus = Bus()

my_bus.get_on_the_bus()

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