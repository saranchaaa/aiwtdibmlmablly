class GreatGrandma:
    age = 90
    height = 159
    x = 55555

class Grandma(GreatGrandma):
    age = 59
    height = 168

class Dad(Grandma):
    age = 38
    height = 175

class Child(Dad):
    age = 12
    name = "nnn"
    height = 164

    def __init__(self):
        print(self.height)
        print(self.name)
        print(self.x)


c = Child()
