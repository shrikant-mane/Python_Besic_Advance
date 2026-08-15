from emp import *
import pickle

f = open("employee.dat", "wb")

while True:
    eno = input("Enter employee number: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    salary = input("Enter salary: ")
    emp_address = input("Enter emp address: ")

    employee = Employee(eno, first_name, last_name, salary, emp_address)
    pickle.dump(employee, f)

    option = input("Do you want to add more employee? (Yes/No): ")
    if option.lower() == "no":
        break

print("Employee object load successfully")

