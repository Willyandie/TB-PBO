import pickle
from survey import Survey

def main():
    data_survey = []
    file_database = "survey_database.dat"

    user_survey_1 = Survey("Willy", "10", "Tidak ada, programnya sudah sangat bagus")
    user_survey_2 = Survey("Arthur", "9", "-")
    user_survey_3 = Survey("Bitha", "5", "Masih banyak yang perlu diperbaiki dari programnya")

    data_survey.append(user_survey_1)
    data_survey.append(user_survey_2)
    data_survey.append(user_survey_3)

    with open(file_database, 'wb') as data:
        pickle.dump(data_survey, data, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()