def count_elem(input_list):
    unique_elements = set()
    duplicate_elements = set()
    for item in input_list:
        if item in unique_elements:
            duplicate_elements.add(item)
            unique_elements.remove(item)
        else:
            unique_elements.add(item)
    
    return len(unique_elements), len(duplicate_elements)

def main():
    my_list = [1, 2, 2, 3, 4, 4, 5]
    unique_count, duplicate_count = count_elem(my_list)
    result = (unique_count, duplicate_count)
    print(result)


if __name__ == "__main__":
    main()