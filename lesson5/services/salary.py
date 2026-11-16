def calculate_bonus(salary):
    bonus = salary * 0.10
    return bonus


def calculate_total_salary(salary):
    bonus = calculate_bonus(salary)
    total = salary + bonus

    return total