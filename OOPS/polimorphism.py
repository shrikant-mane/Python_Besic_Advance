from math import pi

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Cat Info name:{self.name}, age:{self.age}")

    def make_sound(self):
        print("Maew Maew")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Dog Info name:{self.name}, age:{self.age}")

    def make_sound(self):
        print("Bow Bow")

cat = Cat("Chinna", 3)
dog = Dog("Raja", 5)

for animal in(cat, dog):
    animal.info()
    animal.make_sound()



class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am two dimentional shape"

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Square have each angle to 90 degree"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

a = Square(5)
print(a)
b = Circle(7)
print(b)
print(a.area())
print(a.fact())
print(b.area())
print(b.fact())


### Operator Overloading

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days

class Timeshit:
    def __init__(self, name, days):
        self.days = days
        self.name = name

employee = Employee("shrikant", 1000)
Timeshit = Timeshit("shrikant", 30)

print(employee*Timeshit)
