import json
class Employee:
    def __init__(self, employee_id, first_name, last_name, salary, address = None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.address = address

    def display(self):
        print(f"{self.employee_id} {self.first_name} {self.last_name} "
              f"{self.salary} {self.address}")


employee= Employee(1,"shrikant", "mane", 70000, "pune")

emp_dict_data = employee.__dict__

with open("employee.json", 'w') as outfile:
    json.dump(emp_dict_data, outfile, indent=4, sort_keys=True)

print("employee data saved successfully")

with open("employee.json", 'r') as outfile:
    employee_data = json.load(outfile)
    new_employee = Employee(employee_data["employee_id"], employee_data["first_name"],
                            employee_data["last_name"], employee_data["salary"], employee_data["address"])
    new_employee.display()


