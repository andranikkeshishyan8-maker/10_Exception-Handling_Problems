import math

try:
    num = float(input("Enter a number: "))
    
    if num < 0:
        raise ValueError("Number must not be negative.")
    
    print("Square root:", math.sqrt(num))

except ValueError as e:
    print("Error:", e)
