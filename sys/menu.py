from funcs import funcsMenu
from funcs import admin

systemOn = True

while systemOn:
    print("Login Options:")
    print("1 - Login as User")
    print("2 - Login as Seller")
    print("3 - Login as Admin")
    print("0 - Exit System")
    print(" ")

    login = input("Select your option: ")

    if login == "1":  # User Login
        funcsMenu.UserMenu()

    elif login == "2":  # Seller Login
        funcsMenu.SellerMenu()

    elif login == "3":  # Admin Login
        funcsMenu.AdminMenu()

    elif login == "0":  # System Exit
        subsystemOn = True
        while subsystemOn:
            print("Are You Sure You Want to Exit the System?")
            print("0 - Don't Exit the System")
            print("1 - Exit the System")
            print(" ")

            leave = input("Choose Wisely: ")
            if leave == "0":
                print("Amazing! Let's Keep Buying!")
                print(" ")
                break
            elif leave == "1":
                print("See You Next Time!")
                print(" ")
                subsystemOn = False
                systemOn = False
                break
            else:
                print("Invalid Option, Choose Again!")
                print(" ")
    else:
        print("Invalid Login, Try Again!")
        print(" ")
