class Chapter:

    def __init__(self, number, title):
        self.__number = number
        self.__title = title

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, num):
        if isinstance(num, int):
            self.__number = num

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title_name):
        if isinstance(title_name, str):
            self.__title = title_name
