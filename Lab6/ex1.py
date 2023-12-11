import os
import sys

def read_file(file_path):
    try:
        f = open(file_path, "rt")
        print(f.read())
    except OSError:
        print("Error opening file")
    except IOError:
        print("Error reading file")
    finally:
        f.close()

def all_files_with_extension(directory, extension):
    files=[]
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            if filename.endswith(extension):
                files.append(filename)
    return files

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py /path/to/directory file_extension")
    else:
        try:
            directory = sys.argv[1]
            extension = sys.argv[2]
            
            if os.path.isdir(directory) == False:
                raise ValueError("Directorul nu există!")
            if extension[0] != ".":
                raise ValueError("Extensia trebuie sa inceapa cu punct!")

            files = all_files_with_extension(directory, extension)
            files = [os.path.join(directory, file) for file in files]
            for file in files:
                read_file(file)
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()  