import pickle
from user import user

def main():
    dat_user = []
    file_database = "database_user.dat"

    dat_1 = user("6210000", "Willy", "willy.ganteng@gmail.com", "123", "Male", "Jl. Suka Jalan", "0810000")
    dat_2 = user("6210001", "Arthur", "arthur.ganteng@gmail.com", "123", "Male", "Jl. Suka Pukul", "0810001")
    dat_3 = user("6210002", "Bobi", "bobi.ganteng@gmail.com", "123", "Male", "Jl. Suka Terjang", "0810002")
    dat_4 = user("6210003", "Bitha", "bitha.cantik@gmail.com", "123", "Female", "Jl. Suka Tidur", "0810003")
    dat_5 = user("6210004", "Lucky", "lucky.ganteng@gmail.com", "123", "Male", "Jl. Suka Silat", "0810004")

    dat_user.append(dat_1)
    dat_user.append(dat_2)
    dat_user.append(dat_3)
    dat_user.append(dat_4)
    dat_user.append(dat_5)

    with open(file_database, 'wb') as data:
        pickle.dump(dat_user, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()