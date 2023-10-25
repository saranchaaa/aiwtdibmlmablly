class Computer:
    def calculate(self):
        print("Calculating...")


class Display:
    def display(self):
        print("Displaying...")

class Phone(Computer, Display):
    pass


iphone = Phone()

iphone.calculate()
iphone.display()
