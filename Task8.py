class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18 or age > 120:
        raise InvalidAgeError("Age must be between 18 and 120.")


try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError:
    print("Please enter a valid integer.")
except InvalidAgeError as e:
    print("Error:", e)
else:
    print("Age accepted.")
