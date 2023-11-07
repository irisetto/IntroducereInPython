

import os

def error_callback(exception):
    print(f"Error: {str(exception)}")

def search_files(target, to_search, callback=None):
    result = []
    if os.path.isfile(target):
        try:
            with open(target, 'r') as f:
                if to_search in f.read():
                    result.append(target)
        except Exception as e:
            if callback is not None:
                callback(e)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        if to_search in f.read():
                            result.append(file_path)
                except Exception as e:
                    if callback is not None:
                        callback(e)
    else:
        raise ValueError("Target must be a file or directory.")
    return result

def main():
    try:   
        target = "D:\\teo\\Faculty\\III-1\\Introducere in Python\\Lab4\\file_ex2.txt"
        to_search = "Lab4"
        result = search_files(target, to_search, callback=error_callback)
        print(result)
    except Exception as e:
        error_callback(e)

if __name__ == "__main__":
    main()