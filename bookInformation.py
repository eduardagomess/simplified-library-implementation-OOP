from publisher import Publisher
from author import Author
from chapter import Chapter

class Book:
    def __init__(self, code, title, year, publisher, author, chapter_number, chapter_title):
        self.__code = code
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__author = author
        self.__chapter_number = chapter_number
        self.__chapter_title = chapter_title
        self.__authors = [author]
        self.__chapters = [Chapter(chapter_number, chapter_title)]

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, book_code):
        if isinstance(book_code, int):
            self.__code = book_code

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title_name):
        if isinstance(title_name, str):
            self.__title = title_name

    @property
    def year(self):
        return self.__year

    @year.setter
    def ano(self, book_year):
        if isinstance(book_year, int):
            self.__year = book_year

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher_name):
        if isinstance(publisher_name, Publisher):
            self.__publisher = publisher_name

    @property
    def authors(self):
        return self.__authors

    def addAuthor(self, author):
        if isinstance(author, Author):
            if author not in self.__authors:
                self.__authors.append(author)

    def deleteAuthor(self, author):
        if isinstance(author, Author):
            if author in self.__authors:
                self.__authors.remove(author)

    def addChapter(self, number, title):
        chapter = self.findChapterByTitle(title)
        if not isinstance(chapter, Chapter):
            chapter = Chapter(number, title)
            self.__chapters.append(chapter)

    def deleteChapter(self, title):
        chapter = self.findChapterByTitle(title)
        if isinstance(chapter, Chapter):
            if chapter in self.__chapters:
                self.__chapters.remove(chapter)

    def findChapterByTitle(self,title):
        for chapter in self.__chapters:
            if chapter.title == title:
                return chapter
