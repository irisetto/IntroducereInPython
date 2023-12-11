import sys
def read_file(file):
    with open(file, "r") as f:
        data = f.read()
    return data

def reverse_file_content(data):
    with open("file_reverse.txt","w") as f:
        for c in list(reversed(data)):
            f.write(c)

def sorted_words(data):
    word_freq = {}
    for word in data.split():
        word_freq[word]= word_freq.get(word, 0) + 1
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

def frequent_word(data):
    return max(data, key= lambda x: x[1])[0]

def least_frequent_word(data):
    return min(data, key= lambda x: x[1])

def longest_word(data):
    return max(data.split(), key=len)

def sort_words_alpha(data):
    data = [word for word in data.split() if len(word)>1]
    return sorted(data, key= lambda x: (x[1], x[-1]))

def write_file(data):
    with open("answers.txt","w") as f:
        f.write(data)

def main():
    if len(sys.argv) != 2:
        print("python script.py file/path")
    else:
        file = "file.txt"
        data = read_file(file)
        reverse_file_content(data)
        sorted = sorted_words(data)
        print(frequent_word(sorted))
        print(least_frequent_word(sorted))
        print(longest_word(data))
        print(sort_words_alpha(data))
        write_file(data)
        
if __name__ == "__main__":
    main()    