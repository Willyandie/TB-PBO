from database import Database
from admin import Admin
from user import User
from vehicle import Vehicle
from rental import Rental
from survey import Survey
import pickle

def main():
    loop = True # variable to loop the program (bool)
    datab = Database() # variable to assign the class Database()
    admin = Admin() # variable to assign the class Admin()

    # Opening the database of user
    data_user = "user_database.dat"
    with open(data_user, 'rb') as data:
        users = pickle.load(data)

    # Opening the database of vehicle
    data_vehicle = "vehicle_database.dat"
    with open(data_vehicle, "rb") as data:
        vehicles = pickle.load(data)

    # Opening the database of rental
    rental_history = "rental_history.dat"
    with open(rental_history, "rb") as data:
        historys = pickle.load(data)

    # Opening the database of survey
    survey_database = "survey_database.dat"
    with open(survey_database, "rb") as data:
        surveys = pickle.load(data)

    # Main menu of the app
    while (loop == True):
        print("=" * 25)
        print("Vehicle Rental")
        print("=" * 25)
        print("1. Login")
        print("2. Registration")
        print("3. Exit App")
        # Choosing the number of the feature listed in the main menu
        feature = int(input("Choose a feature number (1/2/3) = "))

        # Login Menu
        if (feature == 1):
            loop_login = True
            while (loop_login == True):
                print("=" * 25)
                print("Login as:")
                print("1. User")
                print("2. Admin")
                print("3. Logout")
                # Choosing the role to login to the app
                feature_login = int(input("Choose a number (1/2/3) = "))
                # Login as user
                if (feature_login == 1):
                    print("=" * 25)
                    email = str(input("Email = "))
                    password = str(input("Password = "))

                    # User login validation
                    u_check = False
                    count_user = 0 
                    for user in users:
                        if (email == user.email and password == user.password):
                            u_check = True
                            break
                        count_user += 1
                    # If the user login is valid
                    login_user = True
                    if (u_check == True):
                        while (login_user == True):
                            # Showing the home page of user
                            print("=" * 25)
                            print("USER HOME PAGE")
                            print("=" * 25)
                            print("1. Rent a Vehicle")
                            print("2. Show Vehicle Data")
                            print("3. Survey")
                            print("4. Logout")
                            # Choosing the number of the feature listed above
                            user_feature = int(input("Choose a feature number (1/2/3/4) = "))
                            # If user choose to rent a vehicle
                            if (user_feature == 1):
                                print("=" * 25)
                                print("VEHICLE RENTAL")
                                print("=" * 25)
                                license_plate = str(input("Input License Plate Number = "))

                                # Checking the vehicle availibility
                                status = False
                                count_vehicle = 0
                                for vehicle in vehicles:
                                    if (license_plate == vehicle.license_plate):
                                        status = True
                                        break
                                    count_vehicle += 1

                                # If the vehicle is unavailable
                                if (status == False):
                                    print("=" * 25)
                                    print("SORRY, THE VEHICLE IS CURRENTLY UNAVAILABLE AT THE MOMENT")
                                # If the vehicle is available
                                # User making a payment
                                else:
                                    print("=" * 25)
                                    print(f"Vehicle {vehicles[count_vehicle].license_plate} status")
                                    print(f"Price = {vehicles[count_vehicle].price}")
                                    print("=" * 25)
                                    print("PAYMENT")
                                    payment = False
                                    while (payment == False):
                                        money = int(input("Input amount of money = "))
                                        # If the payment is successfully made
                                        if (money >= vehicles[count_vehicle].price):
                                            print("=" * 25)
                                            print("PAYMENT HAS BEEN SUCCESFUL")
                                            print("=" * 25)
                                            print(f"Name = {users[count_user].name}")
                                            print(f"Rented Vehicle = {vehicles[count_vehicle].license_plate}")
                                            print(f"Vehicle Type = {vehicles[count_vehicle].vehicle_type}")
                                            print("=" * 25)
                                            print("P A I D")
                                            print("=" * 25)

                                            # Assigning the rental data to a variable
                                            new_rental = Rental(users[count_user].name, vehicles[count_vehicle].vehicle_type, vehicles[count_vehicle].price)
                                            # Adding the newly added rental data to the database
                                            historys.append(new_rental)
                                            with open(rental_history, 'wb') as data:
                                                pickle.dump(historys, data, pickle.HIGHEST_PROTOCOL)
                                            payment = True
                                        # If the payment is not succesful
                                        else:
                                            print("=" * 25)
                                            print("PAYMENT FAILED")
                                            print("=" * 25)

                            # If user wishes to see the data of the vehicles
                            elif (user_feature == 2):
                                print("=" * 25)
                                print("SHOWING VEHICLE DATA")
                                print("=" * 25)
                                datab.print_data_vehicle()
                            # If user wishes to fill in the survey 
                            elif (user_feature == 3):
                                print("=" * 25)
                                print("SURVEY PAGE")
                                print("=" * 25)
                                # Filling in the survey
                                rate = str(input("Rate this app (from 1-10) = "))
                                testimony = str(input("Write your testimony (max.100 chars) = "))

                                # Assigning the survey data to a variable
                                new_survey = Survey(users[count_user].name, rate, testimony)
                                # Adding the newly done survey to the survey database
                                surveys.append(new_survey)
                                with open(survey_database, 'wb') as data:
                                    pickle.dump(surveys, data, pickle.HIGHEST_PROTOCOL)

                            # User logging out of the app
                            elif (user_feature == 4):
                                login_user = False

                    # If either the email/password is incorrect
                    else:
                        print("INCORRECT EMAIL OR PASSWORD")

                # Login as Admin
                elif (feature_login == 2):
                    print("=" * 25)
                    email = str(input("Email = "))
                    password = str(input("Password = "))
                    # Admin login validation
                    check = admin.login_admin(email, password)

                    login_admin = True
                    # If the login is valid
                    if (check == True):
                        while (login_admin == True):
                            print("=" * 25)
                            print("ADMIN HOME PAGE")
                            print("1. User Database")
                            print("2. Vehicle Database")
                            print("3. Adding a Vehicle")
                            print("4. Rental History")
                            print("5. Survey Database")
                            print("6. Logout")
                            # Choosing the number of the feature listed above
                            user_feature = int(input("Choose a feature number (1/2/3/4/5/6) = "))
                            # If admin chooses to see the user data
                            if (user_feature == 1):
                                print("=" * 25)
                                print("SHOWING USER DATA")
                                print("=" * 25)
                                datab.print_data_user()
                            # If admin chooses to see the vehicle data
                            elif (user_feature == 2):
                                print("=" * 25)
                                print("SHOWING VEHICLE DATA")
                                print("=" * 25)
                                datab.print_data_vehicle()
                            # If admin wants to add a new vehicle to the database
                            elif (user_feature == 3):
                                print("=" * 25)
                                print("ADDING a VEHICLE")
                                print("=" * 25)
                                # Inserting the vehicle data
                                license_plate = str(input("License Plate Number = "))
                                vehicle_year = str(input("Year of Registration = "))
                                condition = str(input("Condition = "))
                                vehicle_type = str(input("Type of Vehicle = "))
                                price = int(input("Price = "))
                                # Assigning vehicle data to a variable
                                new_vehicle = Vehicle(license_plate, vehicle_year, condition, vehicle_type, price)

                                # Checking the duplication of the vehicle in the database
                                duplicate = False
                                for vehicle in vehicles:
                                    if (new_vehicle.license_plate == vehicle.license_plate):
                                        duplicate = True
                                        break
                                # If the vehicle is not duplicated; The vehicle addition is successful
                                if (duplicate == False):
                                    # Adding the newly added vehicle data to the database
                                    vehicles.append(new_vehicle)
                                    with open(data_vehicle, 'wb') as data:
                                        pickle.dump(vehicles, data, pickle.HIGHEST_PROTOCOL)
                                    print("=" * 25)
                                    print("A NEW VEHICLE HAS BEEN ADDED!")
                                # If the vehicle is already in the database
                                else:
                                    print("=" * 25)
                                    print("LICENSE PLATE NUMBER IS ALREADY IN THE DATABASE")
                                    print("VEHICLE IS NOT ADDED TO THE DATABASE!")
                            # If admin wants to see the history of the user rental
                            elif (user_feature == 4):
                                print("=" * 25)
                                print("SHOWING THE RENTAL HISTORY OF USER")
                                print("=" * 25)
                                datab.print_rental_history()
                            # If admin wants to see the survey done by user
                            elif (user_feature == 5):
                                print("=" * 25)
                                print("SHOWING THE USER SURVEY")
                                print("=" * 25)
                                datab.print_data_survey()
                            # Admin logging out of the app
                            elif (user_feature == 6):
                                login_admin = False
                    # If the login is not valid
                    else:
                        print("=" * 25)
                        print("INCORRECT EMAIL OR PASSWORD")
                # Admin/user logging out of the home page
                elif (feature_login == 3):
                    loop_login = False

        # User doesn't have an account 
        elif (feature == 2):
            print("=" * 25)
            print("REGISTER AN ACCOUNT")
            print("=" * 25)
            # Filling in the user data 
            identity_number = str(input(("Identity Number = ")))
            name = str(input(("Name = ")))
            email = str(input(("Email = ")))
            password = str(input(("Password = ")))
            gender = str(input(("Gender = ")))
            address = str(input(("Address = ")))
            phone_no = str(input(("Phone Number = ")))

            # Assigning user data to a variable 
            new_user = User(identity_number, name, email, password, gender, address, phone_no)

            # Checking the duplication of the user in the database
            duplicate = False
            for user in users:
                if (new_user.email == user.email):
                    duplicate = True
                    break
            # If the data is not duplicated
            if (duplicate == False):
                # Adding the newly added user data to the database
                users.append(new_user)
                with open(data_user, 'wb') as data:
                    pickle.dump(users, data, pickle.HIGHEST_PROTOCOL)
                print("REGISTRATION HAS BEEN SUCCESSFUL!")
            # If the email is not valid
            else:
                print("=" * 25)
                print("EMAIL HAS BEEN USED IN ANOTHER ACCOUNT")
                print("REGISTRATION FAILED!")
        # User/Admin logging out of the app
        elif (feature == 3):
            loop = False

    # The program finished
    print("=" * 25)
    print("PROGRAM FINISHED. THANK YOU")
    print("=" * 25)
    return

if __name__ == '__main__':
    main()