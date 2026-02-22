def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    return number == sum(int(digit) ** num_digits for digit in num_str)

print(is_armstrong(153))  # True
print(is_armstrong(123))  #Fals