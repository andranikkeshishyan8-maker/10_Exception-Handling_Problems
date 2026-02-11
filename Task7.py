def find_max_value(numbers):
    max_value = numbers[0]   
    
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value


data = [-5, -2, -10]
print("Max value:", find_max_value(data))
