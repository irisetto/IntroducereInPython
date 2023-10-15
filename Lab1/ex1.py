
def read_numbers_from_console():
    numbers = []
    input_str = input("Enter numbers separated by spaces: ")
    numbers = [int(num) for num in input_str.split()]

    return numbers

def cmmdc_fun(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def cmmdc_list(numbers):
    if len(numbers)<2:
        return numbers[0]
    
    cmmdc = numbers[0]
    for i in range(1, len(numbers)):
        cmmdc = cmmdc_fun(cmmdc, numbers[i])

    return cmmdc

numbers = read_numbers_from_console()
print(cmmdc_list(numbers))
