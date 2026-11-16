print("hello world")

employees = [
    {"name": "Raj", "salary": 50000},
    {"name": "Priya", "salary": 60000},
    {"name": "Kiran", "salary": 45000}
]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

print(sorted_employees)