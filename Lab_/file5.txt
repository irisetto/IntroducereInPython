import os

def unique_sorted_extensions(director):
    # Verificăm dacă directorul există
    if not os.path.exists(director) or not os.path.isdir(director):
        raise ValueError("Directorul nu există!")

    extensions = set()
    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)):
            extension = os.path.splitext(file)[1][1:] # [1] - extensia, [1:] - fără punct
            extensions.add(extension)
    return sorted(list(extensions))


def main():
    # director = input("Enter a directory: ")
    extensions = unique_sorted_extensions("C:\\Users\\tcohm\\Downloads")
    print(extensions)

if __name__ == "__main__":
    main()