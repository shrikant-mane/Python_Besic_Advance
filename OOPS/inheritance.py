from named_tuple import employee


class Animal:
    """
    base class for animals in inheritance
    """
    def __init__(self, name):
        self.name = name

    def speak(self):
        return (f"{self.name} make a sound")

class Dog(Animal):
    """
    derived class for dog in inheritance
    """
    def speak(self):
        return (f"{self.name} bark")

class Cat(Animal):
    """
    derived class for cat in inheritance
    """
    def speak(self):
        return (f"{self.name} meows")


dog = Dog("Rocky")
cat = Cat("Tom")

print(dog.speak())
print(cat.speak())


### super() method

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"Vehicle :{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def info(self):
        return f"Car info :{super().info()} {self.year}"

class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def info(self):
        return f"Truck info: {super().info()} {self.year}"

car = Car("Ford", "Mustang", 2000)
print(car.info())
truck = Truck("Tom", "Ford", 2020)
print(truck.info())

print(Truck.__mro__)


######
## HAS - A relations --> By using object
#####

class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    def info(self):
        return f"{self.company} {self.model} {self.year}"

class Employee:
    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car
    def info(self):
        print(f"Employee Info: {self.name} {self.age} ")
        print(f"Car info: {self.car.info()} ")

car = Car('Tata', 'Tiago', 2023)
employee = Employee("Shrikant", 28, car)
employee.info()


#############
### HAS -A ---> By using class name
#############


class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    def info(self):
        return f"{self.company} {self.model} {self.year}"

class Employee:
    def __init__(self, name, age, car_company, car_model, purchase_year):
        self.name = name
        self.age = age
        self.car = Car(car_company, car_model, purchase_year)

    def info(self):
        print(f"Employee Info: {self.name} {self.age} ")
        print(f"Car info: {self.car.info()} ")


employee = Employee("Shrikant", 28, 'Tata', 'Tiago', 2023)
employee.info()


#########
##  From Class Method of Child Class, how to call Parent Class Instance Methods
#########
class A:
    def __init__(self):
        print("Parent class Constructor")

    def m1(self):
        print("Parent class instance method")

class B(A):
    @classmethod
    def m2(cls):
        super(B,cls).__init__(cls)
        super(cls,B).m1(cls)

b = B()
b.m2()

    
#########
##  How to Call Parent Class Static Method from Child Class
# StaticMethod by using super()
########

class A:
    def __init__(self):
        print("Parent class constructor")
    def m1(self):
        print("Parent class instance method")

class B(A):
    @staticmethod
    def m2():
        super(B, B).__init__(B)
        super(B, B).m1(B)

b= B()
b.m2()