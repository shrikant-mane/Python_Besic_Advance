class Employee:
    def __init__(self,name, salary, client):

        #Public attribute
        self.name = name

        # Protected attribute
        self._salary = salary

        # Private attribute
        self.__client = client

emp = Employee('Vinay', 14000, 'ABC.Pvt.Ltd')

print(emp.name)

print(emp._salary)
# print(emp.__client) # Error
print(emp.__dict__)
# ==> {'name': 'Vinay', '_salary': 14000, '_Employee__client': 'ABC.Pvt.Ltd'}

print(emp._Employee__client) # To access private attributes


class Department(Employee):
    def __init__(self, name, salary, client):
        super().__init__(name, salary, client)
    def emp_info(self):
        print(f"emp_name: {self.name}")
        print(f"emp_salary: {self._salary}")
        # print(f"client_name :{self.__client}") # Error


emp = Employee('Vinay', 14000, 'ABC.Pvt.Ltd')

department = Department('Vinay', 14000, 'ABC.Pvt.Ltd')
department.emp_info()
