#Employee Records Management

employees = [

    {
        "id": 101,
        "name": "Raj",
        "email": "raj@gmail.com",
        "department": "IT",
        "salary": 45000
    },

    {
        "id": 102,
        "name": "Priya",
        "email": "priya@gmail.com",
        "department": "HR",
        "salary": 50000
    },

    {
        "id": 103,
        "name": "Arun",
        "email": "arun@gmail.com",
        "department": "Finance",
        "salary": 55000
    }

]

# Display all employees

print("EMPLOYEE MANAGEMENT SYSTEM")

for employee in employees:

    print("\nEmployee ID:", employee["id"])

    print("Name:", employee["name"])

    print("Email:", employee["email"])

    print("Department:", employee["department"])

    print("Salary:", employee["salary"])


# Add a new employee

new_employee = {
    "id": 104,
    "name": "Kiran",
    "email": "kiran@gmail.com",
    "department": "IT",
    "salary": 48000
}

employees.append(new_employee)

print("\nUpdated Employee Count:", len(employees))


# Search for an employee

search_name = "Kiran"

for employee in employees:

    if employee["name"] == search_name:

        print("\nEmployee Found")

        print(employee)