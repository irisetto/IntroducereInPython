def most_common_letter(string):
    letters={}
    string = string.lower()
    for char in string:
        if char.isalpha():
            letters[char] = letters.get(char,0)+1
    most_common = max(letters, key=letters.get)
    return most_common, letters[most_common]

print(most_common_letter("an apple is not a tomato"))
