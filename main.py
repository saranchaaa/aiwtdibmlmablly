#code 1
import time
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("Sleep started.")
        time.sleep(2)
        print("...Sleep ended.")
        print("\n")


class Employee(Human):
    def __init__(self, experience, namee, agee):
        super().__init__(namee, agee)
        self.experience = experience


e1 = Employee(0.5, "n1", 22)
print("Name: ", e1.name)
print("Experience: ", e1.experience)
print("Age: ", e1.age)

e1.sleep()
