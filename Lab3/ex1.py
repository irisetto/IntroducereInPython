def list_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_difference_b = set(a) - set(b)
    b_difference_a = set(b) - set(a)

    return [intersection, union, a_difference_b, b_difference_a]

def main():
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]

    result = list_operations(list_a, list_b)
    print(result)

if __name__ == "__main__":
    main()