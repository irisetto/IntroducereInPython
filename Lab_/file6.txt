
import os

def write_files_path(folder_path, file_path):
    with open(file_path, 'w') as f: #with - deschide fisierul si il inchide automat
        for root, _, files in os.walk(folder_path): #os.walk - parcurge recursiv un director 3-tuple (dirpath, dirnames, filenames).
            for file in files:
                if file.startswith('A'):
                    f.write(os.path.join(root, file) + '\n')

def main():
    #folder_path = input("Enter a directory: ")
    #file_path = input("Enter a file: ")
    write_files_path("D:\\teo\\Faculty\\III-1\\Introducere in Python", "D:\\teo\\Faculty\\III-1\\Introducere in Python\\Lab4\\file_ex2.txt")

if __name__ == "__main__":
    main()