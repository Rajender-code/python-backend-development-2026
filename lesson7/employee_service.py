import json


def read_employee():

    try:
        with open("employee.json", "r") as file:
            employee = json.load(file)

        return employee

    except FileNotFoundError:
        print("Employee file not found")
        return None

    except json.JSONDecodeError:
        print("Invalid JSON file")
        return None


def save_employee(employee):

    with open("employee.json", "w") as file:
        json.dump(employee, file, indent=4)

    print("Employee information saved")


def update_salary(salary):

    employee = read_employee()

    if employee is None:
        return

    if salary <= 0:
        raise ValueError("Salary must be greater than zero")

    employee["salary"] = salary

    save_employee(employee)