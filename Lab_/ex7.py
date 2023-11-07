
import os

def file_info(file_path):

    file_info = {
        "full_path": "",
        "file_size": 0,
        "file_extension": "",
        "can_read": False,
        "can_write": False
    }
    file_info["full_path"] = os.path.abspath(file_path)
    file_info["file_size"] = os.path.getsize(file_path)
    file_info["file_extension"] = os.path.splitext(file_path)[1]
    file_info["can_read"] = os.access(file_path, os.R_OK)
    file_info["can_write"] = os.access(file_path, os.W_OK)
    return file_info

def main():
    print(file_info("D:\\teo\\Faculty\\III-1\\Introducere in Python\\Lab4\\ex1.py"))

if __name__ == "__main__":
    main()