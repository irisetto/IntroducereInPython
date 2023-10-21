def palindrome(number):
    return str(number) == str(number)[::-1] #[start:stop:step]
    
def tuple_palindrome(numbers):
    greatest_palindrome = 0
    number_of_palindromes = 0
    for i in numbers:
        if palindrome(i):
            if i > greatest_palindrome:
                greatest_palindrome = i
            number_of_palindromes+=1 
    return (number_of_palindromes,greatest_palindrome)

def main():
    print(tuple_palindrome([121,1,24,44,55,232,4,56,32]))

if __name__ == "__main__":
    main()