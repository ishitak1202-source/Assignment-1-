#System using object-oriented programming principles in Python. This systemshould manage books and patrons (library users), allowing for basic operations suchas adding new books, registering patrons, borrowing books, and returning books.

# Book Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 30)


# Patron Class
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID : {self.patron_id}")
        print(f"Name      : {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)
        else:
            print("No books borrowed.")
        print("-" * 30)


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add Book
    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully!\n")

    # Register Patron
    def register_patron(self):
        patron_id = int(input("Enter Patron ID: "))
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        self.patrons.append(patron)

        print("Patron registered successfully!\n")

    # Find Book
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # Find Patron
    def find_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    # Borrow Book
    def borrow_book(self):
        patron_id = int(input("Enter Patron ID: "))
        book_id = int(input("Enter Book ID: "))

        patron = self.find_patron(patron_id)
        book = self.find_book(book_id)

        if patron is None:
            print("Patron not found.\n")
            return

        if book is None:
            print("Book not found.\n")
            return

        if book.is_borrowed:
            print("Book is already borrowed.\n")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.\n")

    # Return Book
    def return_book(self):
        patron_id = int(input("Enter Patron ID: "))
        book_id = int(input("Enter Book ID: "))

        patron = self.find_patron(patron_id)
        book = self.find_book(book_id)

        if patron is None or book is None:
            print("Invalid Patron ID or Book ID.\n")
            return

        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{patron.name} returned '{book.title}'.\n")
        else:
            print("This patron did not borrow this book.\n")

    # Display Books
    def display_books(self):
        if len(self.books) == 0:
            print("No books in library.\n")
            return

        print("\n------ Library Books ------")
        for book in self.books:
            book.display()

    # Display Patrons
    def display_patrons(self):
        if len(self.patrons) == 0:
            print("No patrons registered.\n")
            return

        print("\n------ Registered Patrons ------")
        for patron in self.patrons:
            patron.display()


# Main Program
library = Library()

while True:
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.add_book()

    elif choice == '2':
        library.register_patron()

    elif choice == '3':
        library.borrow_book()

    elif choice == '4':
        library.return_book()

    elif choice == '5':
        library.display_books()

    elif choice == '6':
        library.display_patrons()

    elif choice == '7':
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
