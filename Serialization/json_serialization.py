import json

employee_data = {
    "emp_id":30,
    "name": "Shrikant",
    "salary": 70000,
    "address": "Pune"
}

json_string = json.dumps(employee_data, indent=4, sort_keys=True)
print(json_string)

with open('employee.json', 'w') as outfile:
    json.dump(employee_data, outfile, indent=4, sort_keys=True)
