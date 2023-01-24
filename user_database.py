import pickle
from user import User

def main():
    data_user = [] # Array to save all the user data 
    # A variable to save the user data that linked to the database
    file_database = "user_database.dat"

    # Assigning data to some variables
    user_1 = User("6210000", "Willy", "willy.ganteng@gmail.com", "123", "Male", "Jl. Suka Jalan", "0810000")
    user_2 = User("6210001", "Arthur", "arthur.ganteng@gmail.com", "123", "Male", "Jl. Suka Pukul", "0810001")
    user_3 = User("6210002", "Bobi", "bobi.ganteng@gmail.com", "123", "Male", "Jl. Suka Terjang", "0810002")
    user_4 = User("6210003", "Bitha", "bitha.cantik@gmail.com", "123", "Female", "Jl. Suka Tidur", "0810003")
    user_5 = User("6210004", "Lucky", "lucky.ganteng@gmail.com", "123", "Male", "Jl. Suka Silat", "0810004")
    
    # Adding the data from the variable to an array
    data_user.append(user_1)
    data_user.append(user_2)
    data_user.append(user_3)
    data_user.append(user_4)
    data_user.append(user_5)

    # Inserting the data from the array to the database
    with open(file_database, 'wb') as data:
        pickle.dump(data_user, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()