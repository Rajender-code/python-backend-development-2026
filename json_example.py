import json

employee = {
    "id": 101,
    "name": "Raj",
    "department": "IT"
}

# Python dictionary to JSON string
json_data = json.dumps(employee)

print(json_data)

# JSON string to Python dictionary
python_data = json.loads(json_data)

print(python_data["name"])
print(python_data["id"])
