class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise "Salary can not be negative"
        self.__salary = value


e = Employee(6000)
print(e.salary)
e.salary = 9000
print(e.salary)
e.salary = -1000
print(e.salary)