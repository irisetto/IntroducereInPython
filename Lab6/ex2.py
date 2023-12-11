import os


def main():
    try:
        directory = "D:\\teo\\Faculty\\III-1\\Introducere in Python\\Lab_"
        if not os.path.exists(directory) and not os.path.isdir(directory):
            raise ValueError("Directorul nu e valid!")
        prefix = 1
        for file in os.listdir(directory):
            string = "file" + str(prefix) + ".txt"
            os.rename(os.path.join(directory, file), os.path.join(directory, string))
            prefix += 1
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()