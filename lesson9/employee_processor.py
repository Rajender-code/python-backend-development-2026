def log_process(function):

    def wrapper(*args, **kwargs):

        print("\nEmployee processing started")

        result = function(*args, **kwargs)

        print("Employee processing completed")

        return result

    return wrapper


class EmployeeProcessor:

    def __init__(self, employees):

        self.employees = employees

    @log_process
    def get_high_salary_employees(self, minimum_salary):

        result = [
            employee
            for employee in self.employees
            if employee["salary"] >= minimum_salary
        ]

        return result

    def sort_employees(self):

        return sorted(
            self.employees,
            key=lambda employee: employee["salary"],
            reverse=True
        )

    def employee_generator(self):

        for employee in self.employees:

            yield employee


def calculate_average_salary(*salaries):

    if not salaries:
        return 0

    return sum(salaries) / len(salaries)