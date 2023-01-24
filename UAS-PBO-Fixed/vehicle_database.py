import pickle
from vehicle import Vehicle

def main():
    data_vehicle = [] # Array to save all the vehicle data
    # A variable to save the vehicle data that linked to the database
    file_database = "vehicle_database.dat"

    # Assigning data to some variables
    vehicle_1 = Vehicle("D 1432 UKM", "2012", "Good", "Car", 700000)
    vehicle_2 = Vehicle("D 1 UKM", "2022", "Very Good", "Car", 900000)
    vehicle_3 = Vehicle("D 52 UKM", "2012", "Bad", "Motorcycle", 100000)
    vehicle_4 = Vehicle("D 17 UKM", "2012", "Good", "Motorcycle", 200000)
    vehicle_5 = Vehicle("D 1945 UKM", "2012", "Bad", "Car", 400000)

    # Adding the data to an array
    data_vehicle.append(vehicle_1)
    data_vehicle.append(vehicle_2)
    data_vehicle.append(vehicle_3)
    data_vehicle.append(vehicle_4)
    data_vehicle.append(vehicle_5)

    # Inserting the data from the array to the database
    with open(file_database, 'wb') as data:
        pickle.dump(data_vehicle, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()