## Anggota Kelompok
# 1. Willyandie Saputra - 2172023
# 2. Tabitha E. Kotambunan - 2172021
# 3. Cristianto Tri Arthurito - 2172027
# 4. Raafi Septyanto - 2172041
# 5. Stevanus Lucky Wijaya - 1872039

class login:
    __email: str
    __password: str
    
    def __init__(self,email, password):
        self.__email = email
        self.__password = password
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self,email):
        self.__email = email
    
    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password


    def changePassword(self, oldPassword, newPassword):
        if (oldPassword == self.getPassword()):
            self.setPassword(newPassword)
            print("Password has successfully been changed")
        else:
            print("Password has not been changed")
