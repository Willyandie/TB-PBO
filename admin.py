## Anggota Kelompok
# 1. Willyandie Saputra - 2172023
# 2. Tabitha E. Kotambunan - 2172021
# 3. Cristianto Tri Arthurito - 2172027
# 4. Raafi Septyanto - 2172041
# 5. Stevanus Lucky Wijaya - 1872039

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

    def print_data_vehicle(self):
        data_vehicle = "database_vehicle.dat"

        with open(data_vehicle, "rb") as data:
            vehicles = pickle.load(data)

        for vehicle in vehicles:
            print(f"Vehicles ID = {vehicle.license_plate}")
            print(f"License Plate = {vehicle.vehicle_year}")
            print(f"Name Vehicles = {vehicle.condition}")
            print(f"vehicle Type = {vehicle.vehicle_type}")
            print(f"Price = {vehicle.price}")
            print("="*25)
