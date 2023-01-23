## Anggota Kelompok
# 1. Willyandie Saputra - 2172023
# 2. Tabitha E. Kotambunan - 2172021
# 3. Cristianto Tri Arthurito - 2172027
# 4. Raafi Septyanto - 2172041
# 5. Stevanus Lucky Wijaya - 1872039

class vehicle:
    __license_plate: str
    __vehicle_year: str
    __condition: str
    __vehicle_type:str
    __price: int

    def __init__(self, license_plate, vehicle_year, condition, vehicle_type, price):
        self.__license_plate = license_plate
        self.__vehicle_year = vehicle_year
        self.__condition = condition
        self.__vehicle_type = vehicle_type
        self.__price = price

    @property
    def license_plate(self):
        return self.__license_plate

    @license_plate.setter
    def license_plate(self, value):
        self.__license_plate = value

    @property
    def vehicle_year(self):
        return self.__vehicle_year

    @vehicle_year.setter
    def vehicle_year(self, value):
        self.__vehicle_year = value

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        self.__condition = value

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
