def count_bits(number):
    return bin(number).count('1')

num = 24
print(count_bits(num))
