# Employee Information System

# Employee details
employee_id = 101
name = "Raj"
email = "raj@gmail.com"
age = 23
salary = 45000.50
department = "IT"
is_active = True

# Store employee information
employee = {
    "employee_id": employee_id,
    "name": name,
    "email": email,
    "age": age,
    "salary": salary,
    "department": department,
    "is_active": is_active
}

# Display employee information
print("EMPLOYEE DETAILS")

print("ID:", employee["employee_id"])
print("Name:", employee["name"])
print("Email:", employee["email"])
print("Age:", employee["age"])
print("Salary:", employee["salary"])
print("Department:", employee["department"])
print("Active:", employee["is_active"])