def is_perfect_number(number):
    if number <= 0:
        return False
    
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisor_sum == number

print(is_perfect_number(28))  # True
print(is_perfect_number(12))  # False