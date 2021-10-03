import re
import os
from unittest import validateEmail,validatePasswd
import database

def welcome():
    print("Welcome to your dashboard")

def gainAccess(Username=None, Password=None):
    Username = input("Enter your username:")
    Password = input("Enter your Password:")
    if not len(Username or Password) < 1:
        if True:
            db = open("database.py", "r")
            d = []
            f = []
            for i in db:
                a= i.split(",")
                c = a
                d.append(a)
            data = d
            # print(data)
            try:
                if data[Username]:
                    try:
                        if Password == data[Username]:
                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                        else:
                            print("Incorrect password or username")
                    except:
                        print("Incorrect password or username")
                else:
                    print("Password or username doesn't exist")
            except:
                print("succefully login!")
        else:
            print("Error logging into the system")
    else:
        print("Please attempt login again")
        gainAccess()
    # b = b.strip()
# accessDb()
def register(Username=None,Email=None, Password1=None, Password2=None):
    Username = input("Enter a username:")
    Email= input("Enter mail:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    db = open("database.py", "r")
    d = []
    for i in db:
        a = i.split(",")
        d.append(a)
    if not len(Password1) <= 8:
        db = open("database.py", "r")
        if not Username == None:
            if len(Username) < 1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists")
                register()
                if not Email == None:
                    if (re.fullmatch(regex, email)):
                        print("Valid Email")
                    elif Email in d:
                        print("Email exists")
                else:
                    print("Invalid Email")
            else:

                if Password1 == Password2:
                    db = open("database.py", "a")
                    db.write(Username + ", " + Password1 +", "+Password2+ "\n")
                    print("User created successfully!")
                    print("Please login to proceed:")
                # print(texts)
                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")

def main(option=None):
    print("Welcome, please select an option")
    option = input("1.Login | 2.Signup:")
    if option == "1":
        gainAccess()

    elif option == "2":
        register()
        gainAccess()

    else:
        print("Please enter a valid parameter, this is case-sensitive")

main()

# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
