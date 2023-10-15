def extract_number(string):
    result = ""
    for i in range(len(string)):
        if string[i].isdigit():
            result += string[i]
            if (i + 1 < len(string) and not string[i + 1].isdigit()) or i + 1 == len(string):
                return result

print(extract_number("abc123ab11c"))
