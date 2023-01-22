class vechile:
    __license_plate: str
    __vechile_year: str
    __condition: str
    __vechile_type:str
    __price: int

    def __init__(self, license_plate, vechile_year, condition, vechile_type, price):
        self.__license_plate = license_plate
        self.__vechile_year = vechile_year
        self.__condition = condition
        self.__vechile_type = vechile_type
        self.__price = price

    @property
    def license_plate(self):
        return self.__license_plate

    @license_plate.setter
    def license_plate(self, value):
        self.__license_plate = value

    @property
    def vechile_year(self):
        return self.__vechile_year

    @vechile_year.setter
    def vechile_year(self, value):
        self.__vechile_year = value

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        self.__condition = value

    @property
    def vechile_type(self):
        return self.__vechile_type

    @vechile_type.setter
    def vechile_type(self, value):
        self.__vechile_type = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value