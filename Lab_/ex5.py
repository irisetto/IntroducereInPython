import os

def search_files(target, to_search):
    result = []
    if os.path.isfile(target):
        with open(target, 'r') as f:
            if to_search in f.read():
                result.append(target)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if to_search in f.read():
                        result.append(file_path)
    else:
        raise ValueError("Target must be a file or directory.")
    return result

def main():
    target = "D:\\teo\\Faculty\\III-1\\Introducere in Python\\Lab4\\file_ex2.txt"
    to_search = "Lab4"
    result = search_files(target, to_search)
    print(result)

if __name__ == "__main__":
    main()