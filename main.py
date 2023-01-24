from database import Database
from admin import Admin
from user import User
from vehicle import Vehicle
from rental import Rental
from survey import Survey
import pickle

def main():
    loop = True
    datab = Database()
    admin = Admin()

    # Membuka database user
    data_user = "user_database.dat"
    with open(data_user, 'rb') as data:
        users = pickle.load(data)

    # Membuka database vehicle
    data_vechile = "vehicle_database.dat"
    with open(data_vechile, "rb") as data:
        vechiles = pickle.load(data)

    # Membuka database rental
    rental_history = "rental_history.dat"
    with open(rental_history, "rb") as data:
        historys = pickle.load(data)

    # Membuka database survey
    survey_database = "survey_database.dat"
    with open(survey_database, "rb") as data:
        surveys = pickle.load(data)

    while (loop == True):
        print("=" * 25)
        print("Sewa Kendaraan")
        print("=" * 25)
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar Aplikasi")

        pilihan = int(input("Silakan input (1/2/3) = "))

        if (pilihan == 1):
            loop_login = True
            while (loop_login == True):
                print("=" * 25)
                print("Login sebagai:")
                print("1. User")
                print("2. Admin")
                print("3. Logout")
                pilihan_login = int(input("Silakan input (1/2/3) = "))
                if (pilihan_login == 1):
                    print("=" * 25)
                    email = str(input("Email = "))
                    password = str(input("Password = "))

                    u_check = False
                    count_user = 0
                    for user in users:
                        if (email == user.email and password == user.password):
                            u_check = True
                            break
                        count_user += 1

                    login_user = True
                    if (u_check == True):
                        while (login_user == True):
                            print("=" * 25)
                            print("USER HOME PAGE")
                            print("1. Menyewa Kendaraan")
                            print("2. Data Kendaraan")
                            print("3. Survey")
                            print("4. Logout")
                            tanya = int(input("Fitur nomor (1/2/3/4) = "))
                            if (tanya == 1):
                                print("=" * 25)
                                print("MENYEWA KENDARAAN")
                                print("=" * 25)
                                license_plate = str(input("License Plate = "))

                                tersedia = False
                                count_vehicle = 0
                                for vechile in vechiles:
                                    if (license_plate == vechile.license_plate):
                                        tersedia = True
                                        break
                                    count_vehicle += 1

                                if (tersedia == False):
                                    print("=" * 25)
                                    print("KENDARAAN TIDAK TERSEDIA")
                                else:
                                    print("=" * 25)
                                    print(f"KENDARAAN {vechiles[count_vehicle].license_plate} TERSEDIA")
                                    print(f"Harga = {vechiles[count_vehicle].price}")
                                    print("=" * 25)
                                    print("PAYMENT")
                                    payment = False
                                    while (payment == False):
                                        money = int(input("Input duit = "))
                                        if (money >= vechiles[count_vehicle].price):
                                            print("=" * 25)
                                            print("PAYMENT BERHASIL")
                                            print("=" * 25)
                                            print(f"Atas Nama = {users[count_user].name}")
                                            print(f"Kendaraan yang disewa = {vechiles[count_vehicle].license_plate}")
                                            print(f"Tipe Kendaraan = {vechiles[count_vehicle].vechile_type}")
                                            print("=" * 25)
                                            print("L U N A S")
                                            print("=" * 25)

                                            new_rental = Rental(users[count_user].name, vechiles[count_vehicle].vechile_type, vechiles[count_vehicle].price)

                                            historys.append(new_rental)
                                            with open(rental_history, 'wb') as data:
                                                pickle.dump(historys, data, pickle.HIGHEST_PROTOCOL)

                                            payment = True
                                        else:
                                            print("=" * 25)
                                            print("PAYMENT GAGAL")
                                            print("=" * 25)

                            elif (tanya == 2):
                                print("=" * 25)
                                print("MENAMPILKAN DATA KENDARAAN")
                                print("=" * 25)
                                datab.print_data_vechile()

                            elif (tanya == 3):
                                print("=" * 25)
                                print("SURVEY")
                                print("=" * 25)

                                rate = str(input("Rate program dari 1-10 = "))
                                testimoni = str(input("Testimoni = "))

                                new_survey = Survey(users[count_user].name, rate, testimoni)

                                surveys.append(new_survey)
                                with open(survey_database, 'wb') as data:
                                    pickle.dump(surveys, data, pickle.HIGHEST_PROTOCOL)

                            elif (tanya == 4):
                                login_user = False

                    else:
                        print("EMAIL ATAU PASSWORD SALAH")

                elif (pilihan_login == 2):
                    print("=" * 25)
                    email = str(input("Email = "))
                    password = str(input("Password = "))

                    check = admin.login_admin(email, password)

                    login_admin = True
                    if (check == True):
                        while (login_admin == True):
                            print("=" * 25)
                            print("ADMIN HOME PAGE")
                            print("1. Database User")
                            print("2. Database Kendaraan")
                            print("3. Menambah Kendaraan")
                            print("4. History Rental")
                            print("5. Database Survey")
                            print("6. Logout")
                            tanya = int(input("Fitur nomor (1/2/3/4/5/6) = "))
                            if (tanya == 1):
                                print("=" * 25)
                                print("MENAMPILKAN DATA USER")
                                print("=" * 25)
                                datab.print_data_user()

                            elif (tanya == 2):
                                print("=" * 25)
                                print("MENAMPILKAN DATA KENDARAAN")
                                print("=" * 25)
                                datab.print_data_vechile()

                            elif (tanya == 3):
                                print("=" * 25)
                                print("MENAMBAH KENDARAAN")
                                print("=" * 25)

                                license_plate = str(input("Nomor Plat = "))
                                vechile_year = str(input("Tahun Kendaraan = "))
                                condition = str(input("Kondisi = "))
                                vechile_type = str(input("Tipe Kendaraan = "))
                                price = int(input("Harga = "))

                                new_vehicle = Vehicle(license_plate, vechile_year, condition, vechile_type, price)

                                duplikat = False
                                for vechile in vechiles:
                                    if (new_vehicle.license_plate == vechile.license_plate):
                                        duplikat = True
                                        break

                                if (duplikat == False):
                                    vechiles.append(new_vehicle)
                                    with open(data_vechile, 'wb') as data:
                                        pickle.dump(vechiles, data, pickle.HIGHEST_PROTOCOL)
                                    print("=" * 25)
                                    print("MENAMBAH KENDARAAN BERHASIL!")
                                else:
                                    print("=" * 25)
                                    print("NOMOR PLAT SUDAH DIGUNAKAN")
                                    print("MENAMBAH KENDARAAN GAGAL!")

                            elif (tanya == 4):
                                print("=" * 25)
                                print("MENAMPILKAN HISTORY RENTAL")
                                print("=" * 25)
                                datab.print_rental_history()

                            elif (tanya == 5):
                                print("=" * 25)
                                print("MENAMPILKAN HISTORY SURVEY")
                                print("=" * 25)
                                datab.print_data_survey()

                            elif (tanya == 6):
                                login_admin = False
                    else:
                        print("=" * 25)
                        print("EMAIL ATAU PASSWORD SALAH")

                elif (pilihan_login == 3):
                    loop_login = False

        elif (pilihan == 2):
            print("=" * 25)
            print("REGISTRASI")
            print("=" * 25)

            identity_number = str(input(("Identity Number = ")))
            name = str(input(("Name = ")))
            email = str(input(("Email = ")))
            password = str(input(("Password = ")))
            gender = str(input(("Gender = ")))
            addres = str(input(("Addres = ")))
            phone_no = str(input(("Phone Number = ")))

            new_user = User(identity_number, name, email, password, gender, addres, phone_no)

            duplikat = False
            for user in users:
                if (new_user.email == user.email):
                    duplikat = True
                    break

            if (duplikat == False):
                users.append(new_user)
                with open(data_user, 'wb') as data:
                    pickle.dump(users, data, pickle.HIGHEST_PROTOCOL)
                print("REGISTRASI BERHASIL!")
            else:
                print("=" * 25)
                print("EMAIL SUDAH DIGUNAKAN")
                print("REGISTRASI GAGAL!")

        elif (pilihan == 3):
            loop = False

    print("=" * 25)
    print("PROGRAM SELESAI")
    return

if __name__ == '__main__':
    main()