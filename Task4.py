filename = input("Enter filename: ")

try:
    file = open(filename, "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Finished file attempt.")
    try:
        file.close()
    except:
        pass
