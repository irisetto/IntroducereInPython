def filtering_elements(*lists):
    result_list = []
    max_length = max(len(lst) for lst in lists)

    for i in range(max_length):
        items = []
        for list in lists:
            if i<len(list):
                items.append(list[i])
            else:
                items.append(None)
        result_list.append(tuple(items))

    return result_list

def main():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c","g"]

    result = filtering_elements(list1, list2, list3)
    print(result)

if __name__ == "__main__":
    main()