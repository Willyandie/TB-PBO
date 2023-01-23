## Anggota Kelompok

# 1. Willyandie Saputra - 2172023

# 2. Tabitha E. Kotambunan - 2172021

# 3. Cristianto Tri Arthurito - 2172027

# 4. Raafi Septyanto - 2172041

# 5. Stevanus Lucky Wijaya - 1872039



from admin import admin

from user import user

import pickle



def main():

    data_user = "database_user.dat"



    print("=" * 25)

    print("Vehicle Rental")

    print("="*25)

    print("1. Login")

    print("2. Registration")

    print("3. Exit App")

    main_menu = int(input("Pick a number (1/2/3) = "))



    while(main_menu != 3):



        if (main_menu == 1):

            print("="*25)

            print("Login as:")

            print("1. User")

            print("2. Admin")

            print("3. Logout")

            validation = int(input("Silakan input (1/2/3) = ")) 

            while (validation != 3):

                if (validation == 1):

                    Admin = admin()

                    login_user = False



                    while (login_user == False):

                        email = str(input("Email = "))

                        password = str(input("Password = "))

                        if (email == "asd" and password == "asd"): # gatau cr nyambungin ke database user

                            us = login.login(email,password)
                            print(us.getEmail())
                            print(us.getPassword()) # ngeprint doang mau liat ke save apa ga
                            print("Succesfully Login")

                            print("=" * 25)

                            print("USER HOME PAGE")

                            print("1. Vehicle Rental")

                            print("2. Available Vehicles")

                            # print("3. Rental History") 

                            print("3. Update Profile")

                            print("0. Logout")

                            feature = int(input("Choose feature number (1/2/3) = "))

                            while (feature != 0):

                                if (feature == 1):

                                    print("=" * 25)

                                    print("Select Vehicle")

                                    print("=" * 25)

                                    Admin.print_data_vehicle()

                                    print("0. Back")

                                    print("=" * 25)

                                    SelVeh = int(input("Select Vehicle ID (0/1/2/3) = "))

                                    if (SelVeh == 1):

                                        print("=" * 25)

                                        print("You choose a Supra car to rent")

                                        print("Rental Price = 700000")

                                        print("=" * 25)

                                        print("Select Payment")

                                        print("=" * 25)

                                        print("1. Cash")

                                        print("2. Debit")

                                        print("0. Back")

                                        pay = int(input("What do you want to pay with? (0/1/2) -> "))

                                        if (pay == 1):

                                            print("=" * 50) # masih manual , soalnya gatau cara ngonekinnya

                                            print("=========== R E N T A L   R E C E I P T ==========")

                                            print("=" * 50)

                                            print ("Name \t\t\t:", "Arthurito")

                                            print ("Rental vehicles \t", "")

                                            print ("-\tLicense Plate = D 1432 UKM")

                                            print ("-\tVehicles Name = Supra")

                                            print ("-\tvehicles Type = Car")

                                            print ("Bill \t\t\t: Rp.700.000")

                                            print ("Payment \t\t: CASH")

                                            print("=" * 50)

                                            print("================ T H A N K   Y O U ===============")

                                            print("=" * 50)

                                        elif (pay == 2):

                                            print("=" * 50) # masih manual , soalnya gatau cara ngonekinnya

                                            print("=========== R E N T A L   R E C E I P T ==========")

                                            print("=" * 50)

                                            print ("Name \t\t\t:", "Arthurito")

                                            print ("Rental vehicles \t", "")

                                            print ("-\tLicense Plate = D 1432 UKM")

                                            print ("-\tVehicles Name = Supra")

                                            print ("-\tVehicles Type = Car")

                                            print ("Bill \t\t\t: Rp.700.000")

                                            print ("Payment \t\t: DEBIT")

                                            print("=" * 50)

                                            print("================ T H A N K   Y O U ===============")

                                            print("=" * 50)



                                elif (feature == 2):

                                    print("=" * 25)

                                    print("Available Vehicles :")

                                    print("=" * 25)

                                    Admin.print_data_vehicle()

                                    print("0. Back")

                                    print("=" * 25)

                                    

                                elif (feature == 3):    # ini buat ganti password cuman belom nyambung sama data base

                                    print("=" * 25)

                                    email1 = str(input("Insert Email: "))

                                    password1 = str(input("Insert Password: "))

                                    S2 = login.login(email1, password1)

                                    print("Email: ", S2.getEmail())

                                    print("Password: ", S2.getPassword())

                                    print("Change Password YES(1) / NO(2)")

                                    password2 = int(input(" "))

                                    if password2 == 2:

                                        print("Email: ", S2.getEmail())

                                        print("Password: ", S2.getPassword())

                                    else:

                                        oldPass = str(input("Insert Old Password : "))

                                        newPass = str(input("Insert New Password : "))

                                        S2.changePassword(oldPass, newPass)



                                print("=" * 25)

                                print("USER HOME PAGE")
                                print("=" * 25)

                                print("1. Vehicle Rental")

                                print("2. Available Vehicles")

                                print("3. Update Profile")

                                print("0. Logout")

                                feature = int(input("Choose feature number (1/2/3) = "))

                        else:

                            print("=" * 25)

                            print("Invalid email or password")

                            print("=" * 25)

                elif (validation == 2):

                    Admin = admin()

                    login_admin = False

                    while(login_admin == False):

                        email = str(input("Email = "))

                        password = str(input("Password = "))

                        if (email == "admin" and password == "admin"):

                            login_admin = True

                            print("Login Successful")



                            print("=" * 25)

                            print("ADMIN HOME PAGE")

                            print("1. User Database")

                            print("2. Vehicles Database")

                            print("3. Logout")

                            feature = int(input("Choose feature number (1/2/3) = "))

                            while (feature != 3):

                                if (feature == 1):

                                    print("=" * 25)

                                    print("SHOWING USER DATA")

                                    print("=" * 25)

                                    Admin.print_data_user()

                                elif (feature == 2):

                                    print("=" * 25)

                                    print("SHOWING VEHICLES DATA")

                                    print("=" * 25)

                                    Admin.print_data_vehicle()



                                print("ADMIN HOME PAGE")

                                print("1. User Database")

                                print("2. Vehicles Database")

                                print("3. Logout")

                                feature = int(input("Choose feature number (1/2/3) = "))



                        else:

                            print("="*25)

                            print("Invalid email or password")

                            print("="*25)



        elif (main_menu == 2):

            check = True

            while (check == True):

                with open(data_user, 'rb') as data:

                    users = pickle.load(data)



                identity_number = str(input(("Identity Number = ")))

                name = str(input(("Name = ")))

                email = str(input(("Email = ")))

                password = str(input(("Password = ")))

                gender = str(input(("Gender = ")))

                address = str(input(("addresss = ")))

                phone_no = str(input(("Phone Number = ")))



                a = user(identity_number, name, email, password, gender, address, phone_no)



                for data in users:

                    if (data.email != user.email):

                        check = False

                    else:

                        print("EMAIL HAS BEEN USED IN ANOTHER ACCOUNT")



                if (check == False):

                    users.append(a)

                    with open(data_user, 'wb') as data:

                        pickle.dump(users, data, pickle.HIGHEST_PROTOCOL)



        print("=" * 25)

        print("Vehicle Rental")

        print("=" * 25)

        print("1. Login")

        print("2. Registration")

        print("3. Exit app")

        main_menu = int(input("Pick a number (1/2/3) = "))



    print("=" * 25)

    print("PROGRAM FINISHED")



    return



if __name__ == '__main__':

    import login

    main()
