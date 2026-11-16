# Employee information

employee_name = "Raj"

salary = 40000

bonus = 5000

deduction = 2000

is_active = True

# Calculate salary

total_salary = salary + bonus

final_salary = total_salary - deduction

# Employee status

if is_active and final_salary >= 40000:

    print("Employee:", employee_name)

    print("Status: Active")

    print("Final Salary:", final_salary)

elif is_active:

    print("Employee:", employee_name)

    print("Status: Active, salary below 40000")

else:

    print("Employee account is inactive")