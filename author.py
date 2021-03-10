class Author:
    def __init__(self, code, name):
        self.__code = code
        self.__name = name

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, author_code):
        if isinstance(author_code, int):
            self.__code = author_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, author_name):
        if isinstance(author_name, str):
            self.__name = author_name
