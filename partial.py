import os
import sys
def read_files_from_directory(directory):
    files = []
    for dirpath, _, filenames in os.walk(directory):
        for file in filenames:
            files.append(file) 
    return files

def longest_file_name(files):
    max_length = max(files, key=len)
    return max_length

def shortest_file_name(files):
    min_length = min(files, key=len)
    return min_length

def first_file_second_letter_c(files):
    for file in files:
        if file[1] == "c":
            return file

def last_file_last_letter_c(files):
    for file in reversed(files):
        if file[-1] == "c":
            return file

def count_files_with_extensions(files):
    extensions = {}
    for file in files:
        extension = os.path.splitext(file)[1]
        extensions[extension] = extensions.get(extension, 0) + 1
    return extensions

def sort_extensions_frequency(extensions):
    sorted_extensions = sorted(extensions.items(), key=lambda x: (x[1], x[0][2]), reverse=True)
    return sorted_extensions

def write_file(extensions):
    with open("D:\\teo\\Faculty\\III-1\\Introducere in Python\\extensions.txt", "w") as f:
        for extension in extensions:
            f.write(f"{extension[0]}: {extension[1]}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
        #python partial.py "D:\\teo\\Faculty\\III-1\\Introducere in Python\\directory"
    else:
        try:
            directory = sys.argv[1]
            if os.path.isdir(directory) == False:
                raise ValueError("Directorul nu este valid!")  
                         
            files = read_files_from_directory(directory)
            print(longest_file_name(files))
            print(shortest_file_name(files))
            print(first_file_second_letter_c(files))
            print(last_file_last_letter_c(files))
            print(count_files_with_extensions(files))
            extensions = sort_extensions_frequency(count_files_with_extensions(files))
            write_file(extensions)

        except ValueError as e:
            print(e)
if __name__ == "__main__":
    main()