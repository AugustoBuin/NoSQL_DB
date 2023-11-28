#
from funcs import funcsProds
from funcs import funcsSellers
from funcs import funcsUsers


def AdminUsersMenu():
    AdmUserMenu = True
    while AdmUserMenu:
        print("Admin Users Menu")
        print("1 - See all Users")
        print("2 - See specific User")
        print("3 - Insert new User")
        print("4 - Update an User")
        print("5 - Delete an User")
        print("0 - Leave")
        print(" ")

        adminUserChoice = input("Select your option: ")

        if adminUserChoice == "1":
            print(" ")
            funcsUsers.Read_all_users()

        elif adminUserChoice == "2":
            print(" ")
            usr = input("Enter the user email: ")
            funcsUsers.Read_user(usr)

        elif adminUserChoice == "3":
            print(" ")
            funcsUsers.Create_user()

        elif adminUserChoice == "4":
            print(" ")
            email = input("Enter the email: ")
            funcsUsers.Update_user(email)

        elif adminUserChoice == "5":
            print(" ")
            email = input("Enter the email: ")
            funcsUsers.Delete_user(email)

        elif adminUserChoice == "0":
            AdmUserMenu = False
            break

        else:
            print("Invalid Option")
            print(" ")


def AdminSellersMenu():
    AdmSellerMenu = True
    while AdmSellerMenu:
        print("Admin Seller Menu")
        print("1 - See all Sellers")
        print("2 - See specific Seller")
        print("3 - Insert new Seller")
        print("4 - Update an Seller")
        print("5 - Delete an Seller")
        print("0 - Leave")
        print(" ")

        adminSellerChoice = input("Select your option: ")

        if adminSellerChoice == "1":
            print(" ")
            # funcsSellers.Read_all_sellers()
            print("Read_all_sellers()")

        elif adminSellerChoice == "2":
            print(" ")
            # funcsSellers.Read_seller()
            print("Read_seller()")

        elif adminSellerChoice == "3":
            print(" ")
            # funcsSellers.Create_seller()
            print("Create_seller()")

        elif adminSellerChoice == "4":
            print(" ")
            # funcsSellers.Update_seller()
            print("Update_seller()")

        elif adminSellerChoice == "5":
            print(" ")
            # funcsSellers.Delete_seller()
            print("Delete_seller()")

        elif adminSellerChoice == "0":
            AdmSellerMenu = False
            break

        else:
            print("Invalid Option")
            print(" ")


def AdminProdsMenu():
    AdmProdMenu = True
    while AdmProdMenu:
        print("Admin Products Menu")
        print("1 - See all products")
        print("2 - See all products of a specific seller")
        print("3 - See specific product")
        print("0 - Leave")
        print(" ")

        adminProdChoice = input("Select your option: ")

        if adminProdChoice == "1":
            print(" ")
            # funcsProds.Read_all_prods()
            print("Read_all_prods()")

        elif adminProdChoice == "2":
            print(" ")
            # funcsProds.Read_prods_bySeller()
            print("Read_prods_bySeller()")

        elif adminProdChoice == "3":
            print(" ")
            # funcsProds.Read_prod()
            print("Read_prod()")

        elif adminProdChoice == "0":
            AdmProdMenu = False
            break

        else:
            print("Invalid Option")
            print(" ")
