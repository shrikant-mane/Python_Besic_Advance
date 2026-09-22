# Q. Find the name of the employee working on the active projects?
# Q. Find the name of the employee who is working on more than one active project?

data = {
    "users": [
        {
            "id": 1,
            "name": "Atharva",
            "department_id": 101
        },
        {
            "id": 2,
            "name": "Rahul",
            "department_id": 102
        },
        {
            "id": 3,
            "name": "Neha",
            "department_id": 101
        },
        {
            "id": 4,
            "name": "Sam",
            "department_id": 103
        }
    ],
    "departments": [
        {
            "id": 101,
            "name": "Engineering",
            "manager_id": 1001
        },
        {
            "id": 102,
            "name": "HR",
            "manager_id": 1002
        },
        {
            "id": 103,
            "name": "Finance",
            "manager_id": 1003
        }
    ],
    "projects": [
        {
            "id": 501,
            "name": "Inventory System",
            "employee_ids": [1, 3],
            "status": "Active"
        },
        {
            "id": 502,
            "name": "Recruitment Portal",
            "employee_ids": [2],
            "status": "Completed"
        },
        {
            "id": 503,
            "name": "Billing System",
            "employee_ids": [1],
            "status": "Active"
        },
        {
            "id": 504,
            "name": "Payroll System",
            "employee_ids": [],
            "status": "Pending"
        }
    ]
}
