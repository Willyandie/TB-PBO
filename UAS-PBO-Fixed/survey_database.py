import pickle
from survey import Survey

def main():
    data_survey = [] # Array to save all the survey data
    # A variable to save the survey data that linked to the database
    file_database = "survey_database.dat"

    # Assigning data to some variables 
    user_survey_1 = Survey("Willy", "10", "The program is already good enough")
    user_survey_2 = Survey("Arthur", "9", "-")
    user_survey_3 = Survey("Bitha", "5", "I think there's still a lot of room for improvement")

    # Adding the data from the variable to an array
    data_survey.append(user_survey_1)
    data_survey.append(user_survey_2)
    data_survey.append(user_survey_3)

    # Inserting the data from the array to the database
    with open(file_database, 'wb') as data:
        pickle.dump(data_survey, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()