
import os
import sys
def unique_extensions(directory):
    extensions = set()
    for filename in os.listdir(directory): #os.listdir - returneaza o lista cu numele fisierelor din director
        if os.path.isfile(os.path.join(directory, filename)):
            extension = os.path.splitext(filename)[1][1:]
            if extension:
                extensions.add(extension)
    return sorted(extensions)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/directory")
    else:
        directory = sys.argv[1]
        print(unique_extensions(directory))


if __name__ == '__main__':
    main()
