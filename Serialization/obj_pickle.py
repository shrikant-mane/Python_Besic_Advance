import pickle

class Employee:
    def __init__(self, name, age, salary, emp_address):
        self.name = name
        self.age = age
        self.salary = salary
        self.emp_address = emp_address

    def display(self):
        print(f"name: {self.name} | age: {self.age} | salary: {self.salary} \
        | emp_address: {self.emp_address}")


employee = Employee("shrikant", 18, 60000, "Pune")

with open("employee.dat", "wb") as file:
    pickle.dump(employee, file)
    print("Employee object dump successfully")

with open("employee.dat", "rb") as file:
    obj = pickle.load(file)
    print("Employee object load successfully")
    obj.display()
    print(obj.emp_address)
    print(obj.name)


