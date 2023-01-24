class User:
    __identity_number: str
    __name: str
    __email: str
    __password: str
    __gender: str
    __address: str
    __phone_no: str

    def __init__(self, identity_number, name, email, password, gender, address, phone_no):
        self.__identity_number = identity_number
        self.__name = name
        self.__email = email
        self.__password = password
        self.__gender = gender
        self.__address = address
        self.__phone_no = phone_no

    @property
    def identity_number(self):
        return self.__identity_number

    @identity_number.setter
    def identity_number(self, value):
        self.__identity_number = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone_no(self):
        return self.__phone_no

    @phone_no.setter
    def phone_no(self, value):
        self.__phone_no = value