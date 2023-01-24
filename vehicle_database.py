import pickle
from vehicle import Vehicle

def main():
    data_vechile = []
    file_database = "vehicle_database.dat"

    vehicle_1 = Vehicle("D 1432 UKM", "2012", "Good", "Car", 700000)
    vehicle_2 = Vehicle("D 1 UKM", "2022", "Very Good", "Car", 900000)
    vehicle_3 = Vehicle("D 52 UKM", "2012", "Bad", "Motorcycle", 100000)
    vehicle_4 = Vehicle("D 17 UKM", "2012", "Good", "Motorcycle", 200000)
    vehicle_5 = Vehicle("D 1945 UKM", "2012", "Bad", "Car", 400000)

    data_vechile.append(vehicle_1)
    data_vechile.append(vehicle_2)
    data_vechile.append(vehicle_3)
    data_vechile.append(vehicle_4)
    data_vechile.append(vehicle_5)

    with open(file_database, 'wb') as data:
        pickle.dump(data_vechile, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()