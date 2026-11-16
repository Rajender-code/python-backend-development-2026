class Employee:

    company = "ABC Technologies"

    def __init__(self, employee_id, name, email, department, salary):

        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    def display_details(self):

        print("\nEmployee Details")
        print("--------------------")

        print("ID:", self.employee_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Company:", self.company)

    def calculate_bonus(self):

        return self.salary * 0.10

    def update_salary(self, new_salary):

        if new_salary <= 0:
            raise ValueError("Salary must be greater than zero")

        self.salary = new_salary

        print("Salary updated successfully")

        