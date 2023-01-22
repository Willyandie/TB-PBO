import pickle

class admin:
    def print_data_user(self):
        data_user = "database_user.dat"

        with open(data_user, "rb") as data:
            users = pickle.load(data)

        for user in users:
            print(f"Identity Number = {user.identity_number}")
            print(f"Name = {user.name}")
            print(f"Email = {user.email}")
            print(f"Password = {user.password}")
            print(f"Gender = {user.gender}")
            print(f"Addres = {user.addres}")
            print(f"Phone Number = {user.phone_no}")
            print("="*25)

    def print_data_vechile(self):
        data_vechile = "database_vechile.dat"

        with open(data_vechile, "rb") as data:
            vechiles = pickle.load(data)

        for vechile in vechiles:
            print(f"License Plate = {vechile.license_plate}")
            print(f"Vechile Year = {vechile.vechile_year}")
            print(f"Condition = {vechile.condition}")
            print(f"Vechile Type = {vechile.vechile_type}")
            print(f"Price = {vechile.price}")
            print("="*25)
