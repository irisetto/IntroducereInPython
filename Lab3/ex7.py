def perform_set_operations(*sets):
    results = {}
    
    for i, a in enumerate(sets): #index si value
        for j, b in enumerate(sets):
            if i != j:
                key_union = f"{a} | {b}"
                key_intersection = f"{a} & {b}"
                key_a_minus_b = f"{a} - {b}"
                key_b_minus_a = f"{b} - {a}"

                union_result = a.union(b)
                intersection_result = a.intersection(b)
                a_minus_b_result = a - b
                b_minus_a_result = b - a

                results[key_union] = union_result
                if intersection_result:
                    results[key_intersection] = intersection_result
                else:
                    results[key_intersection] = "Empty set"

                results[key_a_minus_b] = a_minus_b_result
                results[key_b_minus_a] = b_minus_a_result

    return results

def main():
    set1 = {1, 2}
    set2 = {2, 3}
    set3 = {3, 4}

    result = perform_set_operations(set1, set2, set3)
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()