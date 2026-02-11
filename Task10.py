class InvalidPasswordError(Exception):
    pass


def validate_password(pw):
    if len(pw) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters.")
    if not any(char.isdigit() for char in pw):
        raise InvalidPasswordError("Password must contain at least one digit.")
    if not any(char.isupper() for char in pw):
        raise InvalidPasswordError("Password must contain at least one uppercase letter.")


try:
    password = input("Enter password: ")
    validate_password(password)
except InvalidPasswordError as e:
    print("Error:", e)
else:
    print("Password accepted.")
