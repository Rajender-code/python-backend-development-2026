from employee_processor import (
    EmployeeProcessor,
    calculate_average_salary
)


employees = [
    {"id": 101, "name": "Raj", "salary": 50000},
    {"id": 102, "name": "Priya", "salary": 60000},
    {"id": 103, "name": "Kiran", "salary": 40000},
    {"id": 104, "name": "Arun", "salary": 70000}
]


processor = EmployeeProcessor(employees)


# Filter employees

high_salary = processor.get_high_salary_employees(50000)

print("\nHigh Salary Employees:")

for employee in high_salary:
    print(employee)


# Sort employees

print("\nEmployees Sorted by Salary:")

sorted_employees = processor.sort_employees()

for employee in sorted_employees:
    print(employee)


# Generator

print("\nEmployee Generator:")

for employee in processor.employee_generator():
    print(employee["name"])


# Average salary

average = calculate_average_salary(
    50000,
    60000,
    40000,
    70000
)

print("\nAverage Salary:", average)