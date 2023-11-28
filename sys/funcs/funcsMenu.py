#
from funcs import admin
from funcs import funcsBuys
from funcs import funcsFavs
from funcs import funcsProds
from funcs import funcsSellers
from funcs import funcsUsers


def UserMenu():
    userMenu = True
    while userMenu:
        print("User Menu")
        print("1 - See your information")
        print("2 - Update your information")
        print("3 - Buy something")
        print("4 - See your favorites")
        print("5 - See your last purchases")
        print("0 - Leave")
        print(" ")

        userChoice = input("Select your option: ")
        if userChoice == "1":
            print(" ")
            # funcsUsers.Read_user()
            print("Read User")
        elif userChoice == "2":
            print(" ")
            # funcsUsers.Update_user()
            print("Update User")
        elif userChoice == "3":
            print(" ")
            # funcsBuys.Buying_case()  # dev!!
            print("Buying Case")
        elif userChoice == "4":
            print(" ")
            # funcsFavs.Read_favorites()
            print("Read Favs")
        elif userChoice == "5":
            print(" ")
            # funcsBuys.Read_buys()
            print("Read Buys")
        elif userChoice == "0":
            userMenu = False
            break
        else:
            print("Invalid Option")
            print(" ")


def SellerMenu():
    sellerMenu = True
    while sellerMenu:
        print("Seller Menu")
        print("1 - See your information")
        print("2 - Update your information")
        print("3 - See your products")
        print("4 - Insert new product")
        print("5 - Update a product")
        print("6 - Delete a product")
        print("0 - Leave")
        print(" ")

        sellerChoice = input("Select your option: ")
        if sellerChoice == "1":
            print(" ")
            # funcsSellers.Read_seller()
            print("Read Seller")
        elif sellerChoice == "2":
            print(" ")
            # funcsSellers.Update_seller()
            print("Update Seller")
        elif sellerChoice == "3":
            print(" ")
            # funcsSellers.Read_prods_bySeller()
            print("Read Prods By Seller")
        elif sellerChoice == "4":
            print(" ")
            # funcsProds.Insert_prod()
            print("Insert Prods")
        elif sellerChoice == "5":
            print(" ")
            # funcsProds.Update_prod()
            print("Update Prods")
        elif sellerChoice == "6":
            print(" ")
            # funcsProds.Delete_prod()
            print("Delete Prods")
        elif sellerChoice == "0":
            sellerMenu = False
            break
        else:
            print("Invalid Option")
            print(" ")


def AdminMenu():
    adminMenu = True
    while adminMenu:
        print("Admin Menu")
        print("1 - Manage Users")
        print("2 - Manage Sellers")
        print("3 - Manage Products")
        print("0 - Leave")
        print(" ")

        adminChoice = input("Select your option: ")
        if adminChoice == "1":  # Admin Users Menu
            print(" ")
            admin.AdminUsersMenu()
        elif adminChoice == "2":  # Admin Sellers Menu
            print(" ")
            admin.AdminSellersMenu()
        elif adminChoice == "3":  # Admin Products Menu
            print(" ")
            admin.AdminProdsMenu()
        elif adminChoice == "0":
            adminMenu = False
            break
        else:
            print("Invalid Option")
            print(" ")


#
#
