def main():
    print("Login")
    print("Registrasi")
    validasi = str(input("Silakan input = "))
    if (validasi == "login"):
        email = str(input("Email = "))
        password = str(input("Password = "))
    else:
        # Menuju Halaman  Register
        pass

    return

if __name__ == '__main__':
    main()