def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

def prime_numbers(list):
    prime = []
    for i in list:
        if is_prime(i):
            prime.append(i)
    return prime
    
def main():
    list = [1,2,3,4,5,6,7,8,9,10]
    prime = prime_numbers(list)
    print(f"Prime numbers of list {list} are: {prime}")

if __name__ == "__main__":
    main()
