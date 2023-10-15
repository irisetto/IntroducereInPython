def palindrome(number):
    temp = number
    rev = 0
    while number > 0:
        u = number % 10
        rev = rev*10+u
        number = number//10
    if rev == temp:
        return True
    else:
        return False
    
print(palindrome(1111))
