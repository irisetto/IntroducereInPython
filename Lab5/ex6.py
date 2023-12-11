
class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False
        self.checked_out_by = None
        self.due_date = None

    def check_out(self, user, due_date):
        if not self.checked_out:
            self.checked_out = True
            self.checked_out_by = user
            self.due_date = due_date
            print(f"{self.title} has been checked out by {user} and is due on {due_date}.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            self.checked_out_by = None
            self.due_date = None
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")
        if self.checked_out:
            print(f"Checked out by: {self.checked_out_by}")
            print(f"Due date: {self.due_date}")
        else:
            print("Available for checkout.")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"DVD duration: {self.duration}")

class Magazine(LibraryItem):
    def __init__(self, title, theme, item_id):
        super().__init__(title, "Unknown", item_id) 
        self.theme = theme

    def display_info(self):
        super().display_info()
        print(f"Theme: {self.theme}")

def main():
    book = Book(title="Cei 4 mari", author="Agatha Christie", item_id="B001", num_pages=180)
    book.display_info()
    book.check_out("John", "2021-10-10")
    book.return_item()

    dvd = DVD(title="Inception", director="Christopher Nolan", item_id="D001", duration=148)
    dvd.display_info()
    dvd.check_out("John", "2021-10-10")
    dvd.check_out("John", "2021-10-10")
    dvd.return_item()

    magazine = Magazine(title="National Geographic", theme="Animals", item_id="M001")
    magazine.display_info()
    magazine.check_out("John", "2021-10-10")

if __name__ == "__main__":
    main()