def count_items(x, *lists):
    items = {} # dictionary
    for list in lists:
        for item in list:
            if item in items:
                items[item] += 1 
            else:
                items[item] = 1 
    result = []
    for item, count in items.items():
        if count == x:
            result.append(item)
    return result
def main():
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [4, 5, "test"]
    list4 = [4, 1, "test"]
    x = 2

    result = count_items(x, list1, list2, list3, list4)
    print(result)

if __name__ == "__main__":
    main()