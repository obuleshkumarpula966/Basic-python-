def is_palindrome(number):
    return str(number) == str(number)[::-1]

print(is_palindrome(121))  # True
print(is_palindrome(123))  # False