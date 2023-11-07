import os

def get_absolute_file_paths(dir_path):
    file_paths = []
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            file_paths.append(os.path.abspath(os.path.join(dir_path, file)))
    return file_paths

def main():
    dir_path = "D:\\teo\\Faculty\\III-1\\Introducere in Python"
    result = get_absolute_file_paths(dir_path)
    print(result)

if __name__ == "__main__":  
    main()