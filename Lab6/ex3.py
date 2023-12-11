import sys
import os

def total_size_of_files(directory):
    try:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for file in filenames:
                path = os.path.join(dirpath, file)
                total_size += os.stat(path).st_size
        return total_size
    except FileNotFoundError:
        print("Fisierul nu exista!")
    except PermissionError:
        print("Nu aveti permisiunea de a accesa fisierul!")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
    else:
        try:
            directory = sys.argv[1]
            
            if os.path.isdir(directory) == False:
                raise ValueError("Directorul nu este valid!")
            
            print(total_size_of_files(directory))

        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()  