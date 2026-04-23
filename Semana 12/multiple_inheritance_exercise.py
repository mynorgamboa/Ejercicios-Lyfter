#Herencia funciona para adquirir atributos de distintas clases 
#que son útiles para el objeto que estamos utilizando o creando.

class Swim:

    def swimming(self):
        print('I can swim!')

class Walk:

    def walking(self):
        print('I can walk!')

class Penguin(Swim,Walk):
    def __init__(self):
        print('Im the new Penguin Máximo and I have inheritance from multiple classes!')
        pass


penguin = Penguin()

penguin.swimming()
penguin. walking()