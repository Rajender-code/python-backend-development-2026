"""def employee_details():
    print("Employee Name: Raj")
    print("Department: IT")


def company_details():
    print("Company: ABC Technologies")


employee_details()
company_details() """

"""def employee_details(name, department):
    print("Name:", name)
    print("Department:", department)


employee_details("Raj", "IT") """

"""


def calculate_total(*salaries):

    total = sum(salaries)

    return total


result = calculate_total(30000, 40000, 50000)

print("Total:", result)

  """

# Python provides *args to collect multiple positional arguments into a tuple.

"""def calculate_total(*salaries):

    total = sum(salaries)

    return total


result = calculate_total(30000, 40000, 50000)

print("Total:", result) """

#**kwargs collects multiple keyword arguments into a dictionary.


def employee_details(**details):

    for key, value in details.items():

        print(key, ":", value)


employee_details(
    name="Raj",
    department="IT",
    salary=45000,
    city="Hyderabad"
)