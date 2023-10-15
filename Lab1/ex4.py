def convert_string(word):
    result = ""
    for letter in word:
        if letter.isupper():
            result += '_'
            result += letter.lower()
        else:
            result += letter

    return result.lstrip('_')

print(convert_string("AbraCaDabra"))
