import json

json_string= """
{
    "address": "Pune",
    "emp_id": 30,
    "name": "Shrikant",
    "salary": 70000
}"""

employee_dict = json.loads(json_string)
print(dict(employee_dict))
for k,v in employee_dict.items():
    print("{}:{}".format(k,v))

print("data from json file")
with open("employee.json", 'r') as data_file:
    employee_data = json.load(data_file)
print(type(employee_data["emp_id"]))
