try:
    x = int(input("Enter an integer: "))
    result = 100 / x
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Result:", result)
