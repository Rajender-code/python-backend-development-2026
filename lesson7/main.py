from employee_service import read_employee, update_salary


try:

    employee = read_employee()

    if employee is not None:

        print("Employee Details:")
        print(employee)

        print("\nUpdating salary...")

        update_salary(65000)

        updated_employee = read_employee()

        print("\nUpdated Employee:")
        print(updated_employee)

except ValueError as error:

    print("Error:", error)