class Admin:
    def login_admin(self, email, password):
        check = False
        # Default email & password for admin
        if(email == "admin" and password == "123"):
            check = True
        return check