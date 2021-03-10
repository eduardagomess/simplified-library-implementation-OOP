from bookInformation import Book


class Library:

    def __init__(self):
        self.__books = []

    @property
    def books(self):
        return self.__books

    def addBook(self, book):
        if isinstance(book, Book):
            if book not in self.__books:
                self.__books.append(book)

    def deleteBook(self, book):
        if isinstance(book, Book):
            if book in self.__books:
                self.__books.remove(book)
