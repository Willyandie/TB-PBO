import pickle

class Database:
    # Method to print the user database
    def print_data_user(self):
        # a variable to save the user data that linked to the database
        data_user = "user_database.dat"

        # Opening the user data
        with open(data_user, "rb") as data:
            users = pickle.load(data)
        # Printing the user data
        for user in users:
            print(f"Identity Number = {user.identity_number}")
            print(f"Name = {user.name}")
            print(f"Email = {user.email}")
            print(f"Password = {user.password}")
            print(f"Gender = {user.gender}")
            print(f"Address = {user.address}")
            print(f"Phone Number = {user.phone_no}")
            print("=" * 25)

    # Method to print the vehicle database
    def print_data_vehicle(self):
        # a variable to save the vehicle data that linked to the database
        data_vehicle = "vehicle_database.dat"

        # Opening the vehicle data
        with open(data_vehicle, "rb") as data:
            vehicles = pickle.load(data)
        # Printing the vehicle data
        for vehicle in vehicles:
            print(f"License Plate = {vehicle.license_plate}")
            print(f"Vehicle Year = {vehicle.vehicle_year}")
            print(f"Condition = {vehicle.condition}")
            print(f"Vehicle Type = {vehicle.vehicle_type}")
            print(f"Price = {vehicle.price}")
            print("=" * 25)
    # Method to print the rental history
    def print_rental_history(self):
        # a variable to save the rental history data that linked to the database
        rental_history = "rental_history.dat"

        # Opening the rental history
        with open(rental_history, "rb") as data:
            historys = pickle.load(data)
        # Printing the rental history 
        for history in historys:
            print(f"Name = {history.name}")
            print(f"Vehicle Type = {history.vehicle_type}")
            print(f"Price = {history.price}")
            print("=" * 25)

    # Method to print the survey done by user
    def print_data_survey(self):
        # a variable to save the survey data that linked to the database
        survey_database = "survey_database.dat"

        # Opening the survey data 
        with open(survey_database, "rb") as data:
            surveys = pickle.load(data)
        # Printing the survey
        for survey in surveys:
            print(f"Name = {survey.name}")
            print(f"Rate = {survey.rate}")
            print(f"Testimony = {survey.testimony}")
            print("=" * 25)