def filter_characters(x=1, strings=[], flag=True):
    result_lists = []
    for string in strings:
        char_list = []
        for char in string:
            if (ord(char) % x == 0) if flag else (ord(char) % x != 0): 
                char_list.append(char)
        result_lists.append(char_list)
    return result_lists

def main():
    strings = ["test", "hello", "lab002"]
    x = 2
    flag = False
    result = filter_characters(x, strings, flag)
    print(result)

if __name__ == "__main__":
    main()
