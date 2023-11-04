def list_operations(a, b):
    # Intersection
    intersection = []
    for x in a:
        if x in b:
            intersection.append(x)
    # Union
    union = list(a)
    for x in b:
        if x not in union:
            union.append(x)

    # Elements in a but not in b
    a_minus_b = [x for x in a if x not in b]

    # Elements in b but not in a
    b_minus_a = [x for x in b if x not in a]

    return intersection, union, a_minus_b, b_minus_a

def main():
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]

    intersection, union, a_minus_b, b_minus_a = list_operations(list_a, list_b)
    print("Intersection:", intersection)
    print("Union:", union)
    print("Elements in a but not in b:", a_minus_b)
    print("Elements in b but not in a:", b_minus_a)

if __name__ == "__main__":
    main()
#refa