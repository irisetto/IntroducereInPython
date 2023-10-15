def number_of_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1

    return count

print(number_of_vowels("abracadabra"))
