class Book:
    # Static attribute to track the total number of books
    total_books = 0

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
        # Increment the total_books counter whenever a new book is created
        Book.total_books += 1

    def display_info(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}")

    @staticmethod
    def get_total_books():
        return Book.total_books


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")

print(book1.display_info())
print()
print(book2.display_info())

print(f"Total number of books in the library: {Book.get_total_books()}")