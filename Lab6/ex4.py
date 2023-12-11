import sys
import os

def number_of_files_with_extension(directory):
    extension_count = {}
    if os.listdir(directory) == []:
        raise ValueError("Directorul este gol!")
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            extension = os.path.splitext(filename)[1]
            extension_count[extension] = extension_count.get(extension, 0) + 1
    return extension_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
    else:
        try:
            directory = sys.argv[1]
            
            if os.path.isdir(directory) == False:
                raise ValueError("Directorul nu este valid!")
            print(number_of_files_with_extension(directory))

        except PermissionError:
            print("Nu aveti permisiunea de a accesa fisierul!")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()  