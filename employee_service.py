# Employee records

employees = [

    {
        "id": 101,
        "name": "Raj",
        "department": "IT",
        "salary": 45000
    },

    {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "salary": 50000
    },

    {
        "id": 103,
        "name": "Arun",
        "department": "Finance",
        "salary": 55000
    }

]


# Function 1: Display all employees

def display_employees():

    for employee in employees:

        print(employee)


# Function 2: Add an employee

def add_employee(employee_id, name, department, salary):

    employee = {

        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary

    }

    employees.append(employee)

    return employee


# Function 3: Search employee

def search_employee(employee_id):

    for employee in employees:

        if employee["id"] == employee_id:

            return employee

    return None


# Function 4: Calculate bonus

def calculate_bonus(salary, percentage=10):

    bonus = salary * percentage / 100

    return bonus


# Function 5: Calculate total salary

def calculate_total_salary(salary, bonus):

    return salary + bonus


# Add employee

new_employee = add_employee(
    104,
    "Kiran",
    "IT",
    48000
)

print("New Employee:", new_employee)


# Search employee

result = search_employee(104)

print("Search Result:", result)


# Calculate salary

bonus = calculate_bonus(48000)

total = calculate_total_salary(48000, bonus)

print("Bonus:", bonus)

print("Total Salary:", total)


# Display all employees

print("\nALL EMPLOYEES")

display_employees()