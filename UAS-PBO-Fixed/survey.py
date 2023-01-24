class Survey:
    __name: str
    __rate: str
    __testimony: str

    def __init__(self, name, rate, testimony):
        self.__name = name
        self.__rate = rate
        self.__testimony = testimony

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        self.__rate = value

    @property
    def testimony__testimony(self):
        return self.__testimony
    
    @testimony__testimony.setter
    def testimony__testimony(self, value):
        self.__testimony = value