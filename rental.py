class Rental:
    __name: str
    __vehicle_type: str
    __price: int

    def __init__(self, name, vehicle_type, price):
        self.__name = name
        self.__vehicle_type = vehicle_type
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def vehicle_type(self):
        return self.__vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self.__vehicle_type = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value