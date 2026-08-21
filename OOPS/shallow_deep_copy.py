import copy


class Address:
    def __init__(self, city):
        self.city = city


class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address("Pune")

student1 = Student("Rahul", address)

# Shallow copy
student2 = copy.copy(student1)

# Deep copy
student3 = copy.deepcopy(student1)


print("Student objects:")
print(student1 is student2)
print(student1 is student3)

print("\nAddress objects:")
print(student1.address is student2.address)
print(student1.address is student3.address)