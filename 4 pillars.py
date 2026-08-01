from abc import ABC, abstractmethod

# 1. Encapsulation
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author   # private attribute

    def get_author(self):
        return self.__author

    def __str__(self):
        return f"{self.title} by {self.__author}"


# 2. Inheritance
class User:
    def __init__(self, name):
        self.name = name

class Student(User):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class Teacher(User):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# 3. Polymorphism
class Librarian:
    def issue_book(self, user):
        return f"Book issued to {user.name}"

class DigitalLibrarian(Librarian):
    def issue_book(self, user):
        return f"E-book issued to {user.name}"


# 4. Abstraction
class LibrarySystem(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

class MyLibrary(LibrarySystem):
    def __init__(self):
        self.books = []





#OUTPUT

Python Basics by Alice
Alice
Ishita 21
Alice Computer Science
Book issued to Ishita
E-book issued to Joey
Python Basics by Alice added to library

    def add_book(self, book):
        self.books.append(book)
        return f"{book} added to library"
