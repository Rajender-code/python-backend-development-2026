from employee import Employee


# Create employee objects

employee1 = Employee(
    101,
    "Raj",
    "raj@gmail.com",
    "IT",
    50000
)

employee2 = Employee(
    102,
    "Priya",
    "priya@gmail.com",
    "HR",
    60000
)


# Display employees

employee1.display_details()

employee2.display_details()


# Calculate bonus

print("\nRaj Bonus:", employee1.calculate_bonus())


# Update salary

employee1.update_salary(65000)


# Display updated employee

employee1.display_details()


