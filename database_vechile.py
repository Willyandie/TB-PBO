import pickle
from vechile import vechile

def main():
    dat_vechile = []
    file_database = "database_vechile.dat"

    dat_1 = vechile("D 1432 UKM", "2012", "Good", "Car", 700000)
    dat_2 = vechile("D 1 UKM", "2022", "Very Good", "Car", 900000)
    dat_3 = vechile("D 52 UKM", "2012", "Bad", "Motorcycle", 100000)
    dat_4 = vechile("D 17 UKM", "2012", "Good", "Motorcycle", 200000)
    dat_5 = vechile("D 1945 UKM", "2012", "Bad", "Car", 400000)

    dat_vechile.append(dat_1)
    dat_vechile.append(dat_2)
    dat_vechile.append(dat_3)
    dat_vechile.append(dat_4)
    dat_vechile.append(dat_5)

    with open(file_database, 'wb') as data:
        pickle.dump(dat_vechile, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()