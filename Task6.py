import json

try:
    user_input = input("Enter JSON string: ")
    data = json.loads(user_input)
    print("Age:", data["age"])
except json.JSONDecodeError:
    print("Invalid JSON format.")
except KeyError:
    print("Missing 'age' key.")
