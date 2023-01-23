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
    print("Sewa Kendaraan")
    print("="*25)
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar Aplikasi")
    login_registrasi = int(input("Silakan input (1/2/3) = "))

    while(login_registrasi != 3):

        if (login_registrasi == 1):
            print("="*25)
            print("Login sebagai:")
            print("1. User")
            print("2. Admin")
            print("3. Logout")
            validasi = int(input("Silakan input (1/2/3) = "))
            while (validasi != 3):
                if (validasi == 1):
                    # email = str(input("Email = "))
                    # password = str(input("Password = "))
                    pass
                elif (validasi == 2):
                    Admin = admin()
                    login_admin = False
                    while(login_admin == False):
                        email = str(input("Email = "))
                        password = str(input("Password = "))
                        if (email == "admin" and password == "admin"):
                            login_admin = True
                            print("Login Berhasil")

                            print("=" * 25)
                            print("ADMIN HOME PAGE")
                            print("1. Database User")
                            print("2. Database Kendaraan")
                            print("3. Logout")
                            tanya = int(input("Fitur nomor (1/2/3) = "))
                            while (tanya != 3):
                                if (tanya == 1):
                                    print("=" * 25)
                                    print("MENAMPILKAN DATA USER")
                                    print("=" * 25)
                                    Admin.print_data_user()
                                elif (tanya == 2):
                                    print("=" * 25)
                                    print("MENAMPILKAN DATA KENDARAAN")
                                    print("=" * 25)
                                    Admin.print_data_vechile()

                                print("ADMIN HOME PAGE")
                                print("1. Database User")
                                print("2. Database Kendaraan")
                                print("3. Logout")
                                tanya = int(input("Fitur nomor = (1/2/3) = "))

                        else:
                            print("="*25)
                            print("Email atau Password salah")
                            print("="*25)

        elif (login_registrasi == 2):
            check = True
            while (check == True):
                with open(data_user, 'rb') as data:
                    users = pickle.load(data)

                identity_number = str(input(("Identity Number = ")))
                name = str(input(("Name = ")))
                email = str(input(("Email = ")))
                password = str(input(("Password = ")))
                gender = str(input(("Gender = ")))
                addres = str(input(("Addres = ")))
                phone_no = str(input(("Phone Number = ")))

                a = user(identity_number, name, email, password, gender, addres, phone_no)

                for data in users:
                    if (data.email != user.email):
                        check = False
                    else:
                        print("EMAIL SUDAH DIGUNAKAN")

                if (check == False):
                    users.append(a)
                    with open(data_user, 'wb') as data:
                        pickle.dump(users, data, pickle.HIGHEST_PROTOCOL)

        print("=" * 25)
        print("Sewa Kendaraan")
        print("=" * 25)
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar Aplikasi")
        login_registrasi = int(input("Silakan input (1/2/3) = "))

    print("=" * 25)
    print("PROGRAM SELESAI")

    return

if __name__ == '__main__':
    main()
