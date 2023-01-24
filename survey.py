class Survey:
    __name: str
    __rate: str
    __testimoni: str

    def __init__(self, name, rate, testimoni):
        self.__name = name
        self.__rate = rate
        self.__testimoni = testimoni

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
    def testimoni(self):
        return self.__testimoni
    
    @testimoni.setter
    def testimoni(self, value):
        self.__testimoni = value