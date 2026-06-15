class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def CheckUser(self,username):
        while True:
            username = input("Please enter your username: ")
            len_username = len(username)
            if len_username >= 4:
                special = True
                for letter in username:
                    if letter in "!£$%&=?@*":
                        special = False
                if special:
                        print("Username is valid")
                        break
                else:
                    print("The username must not contain a special character.")
            else:
                print("Username must be at least 4 characters long.")


    def CheckPassword(self,password):
        while True:
            password = input("Enter Password: ")
            len_password = len(password)

            if len_password >= 8:
                num = False
                cap = False
                special_char = False
                for car in password:
                    if car in "0123456789":
                        num = True
                    if car.isupper():
                        cap = True
                    if car in "!£$%&=?@*":
                        special_char = True
                if num and cap and special_char:
                    print("Password is valid")
                    break
                else:
                    print("The password must contain a number, an uppercase letter, and a special character.")
            else:
                print("Password must be at least 8 characters long.")


User = User("username", "password")
User.CheckUser("username")
User.CheckPassword("password")