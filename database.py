import pickle

class Database:
    def print_data_user(self):
        data_user = "user_database.dat"

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
            print("=" * 25)

    def print_data_vechile(self):
        data_vechile = "vehicle_database.dat"

        with open(data_vechile, "rb") as data:
            vechiles = pickle.load(data)

        for vechile in vechiles:
            print(f"License Plate = {vechile.license_plate}")
            print(f"Vechile Year = {vechile.vechile_year}")
            print(f"Condition = {vechile.condition}")
            print(f"Vechile Type = {vechile.vechile_type}")
            print(f"Price = {vechile.price}")
            print("=" * 25)

    def print_rental_history(self):
        rental_history = "rental_history.dat"

        with open(rental_history, "rb") as data:
            historys = pickle.load(data)

        for history in historys:
            print(f"Nama = {history.name}")
            print(f"Vechile Type = {history.vehicle_type}")
            print(f"Price = {history.price}")
            print("=" * 25)