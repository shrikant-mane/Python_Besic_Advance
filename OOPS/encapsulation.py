## Public attributes
class Employee:
    def __init__(self, name):
        self.name = name

employee = Employee("shrikant")
print(employee.name)
employee.name = "Vinay"
print(employee.name)


## Private attributes
class Employee:
    def __init__(self, name, salary, account_number):
        self.name = name
        self._salary = salary
        self.__account_number = account_number
    def info(self):
        return f"{self.name} {self._salary} {self.__account_number}"
employee = Employee("shrikant", 1000, 1234565432)
print(employee.info())
employee.name = "Vinay"
print(employee.name)
print(employee._salary)
employee._salary = 9000
print(employee.info())
employee.__account_number = 9876543456
print(employee.info())
# print(employee._account_number)


class Employee_sal:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

employee = Employee_sal(6000)
print(employee.salary)
employee.salary = 9000
print(employee.salary)



