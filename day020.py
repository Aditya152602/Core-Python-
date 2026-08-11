# import math
# math.floor
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

e = Employee("Aditya Dwivedi",1000000)
print(e.first_name())  