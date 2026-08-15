class Employee:
    def __init__(self, eno, first, last, salary, emp_address):
        self.eno = eno
        self.first = first
        self.last = last
        self.salary = salary
        self.emp_address = emp_address

    def display(self):
        print(f"ENO: {self.eno} | first_name: {self.first} | last_name: {self.last}")
        print(f"salary: {self.salary} | emp_address: {self.emp_address}")
        
