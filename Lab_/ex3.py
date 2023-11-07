
import os

def get_file_content_or_extensions_count(my_path):
    if os.path.isfile(my_path):
        with open(my_path, 'r') as f:
            content = f.read()
            return content[-20:]
    elif os.path.isdir(my_path):
        extensions_count = {}
        for _, _, files in os.walk(my_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                extensions_count[extension] = extensions_count.get(extension, 0) + 1

        sorted_extensions_count = sorted(extensions_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_extensions_count
    else:
        return "Invalid path"

def main():
    result = get_file_content_or_extensions_count("D:\\teo\\Faculty\\III-1\\Introducere in Python")
    print(result)

if __name__ == "__main__":
    main()