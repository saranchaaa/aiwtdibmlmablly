class GreatGrandma:
    age = 90
    height = 159

class Grandma(GreatGrandma):
    age = 59
    height = 168

class Dad(Grandma):
    age = 38
    height = 175

class Child(Dad):
    age = 12
    height = 164

c1 = Child()
print("AGE     HEIGHT")
print(c1.age, "  \t", c1.height)