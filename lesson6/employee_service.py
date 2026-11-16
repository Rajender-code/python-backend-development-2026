from employee_data import employees


def get_employee(employee_id):

    for employee in employees:

        if employee["id"] == employee_id:
            return employee

    raise ValueError("Employee not found")


def add_employee(name, age, salary):

    if not name:
        raise ValueError("Name is required")

    if age < 18:
        raise ValueError("Age must be at least 18")

    if salary <= 0:
        raise ValueError("Salary must be greater than zero")

    new_employee = {
        "id": len(employees) + 101,
        "name": name,
        "age": age,
        "salary": salary
    }

    employees.append(new_employee)

    return new_employee


def calculate_bonus(employee_id):

    employee = get_employee(employee_id)

    return employee["salary"] * 0.10