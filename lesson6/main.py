from employee_service import (
    get_employee,
    add_employee,
    calculate_bonus
)


try:
    employee = get_employee(101)

    print("Employee:", employee)

    bonus = calculate_bonus(101)

    print("Bonus:", bonus)

    new_employee = add_employee("Kiran", 24, 45000)

    print("New Employee:", new_employee)

except ValueError as error:

    print("Application Error:", error)

finally:

    print("Employee Management Process Completed")