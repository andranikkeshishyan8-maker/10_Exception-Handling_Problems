items = ["apple", "banana", "cherry"]

try:
    index = int(input("Enter index: "))
    print("Item:", items[index])
except ValueError:
    print("Index must be an integer.")
except IndexError:
    print("Index out of range.")
