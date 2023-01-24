import pickle
from rental import Rental

def main():
    history = [] # Array to save all the data of the rental history

    # A variable to save the user rental history data that linked to the database
    file_database = "rental_history.dat"

    # Asssigning data to some variables
    rental_1 = Rental("Willy", "Car", 600000)
    rental_2 = Rental("Arthur", "Motorcyle", 200000)
    rental_3 = Rental("Bobi", "Car", 600000)
    rental_4 = Rental("Bitha", "Car", 500000)
    rental_5 = Rental("Lucky", "Motorcyle", 150000)
    
    # Adding the data from the variable to an array
    history.append(rental_1)
    history.append(rental_2)
    history.append(rental_3)
    history.append(rental_4)
    history.append(rental_5)

    # Inserting the data from the array to the database
    with open(file_database, 'wb') as data:
        pickle.dump(history, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()