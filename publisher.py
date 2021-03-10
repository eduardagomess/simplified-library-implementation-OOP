class Publisher:
    def __init__(self, code, name):
        self.__code = code
        self.__name = name

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, publisher_code):
        if isinstance(publisher_code, int):
            self.__code = publisher_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, publisher_name):
        if isinstance(publisher_name, str):
            self.__name = publisher_name
