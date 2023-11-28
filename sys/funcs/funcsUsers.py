import connection

global db
db = connection.client.Beelieve


def Create_user():
    global db
    mycol = db.users
    print("\nInserting a new User")
    name = input("Full Name: ")
    email = input("Email: ")
    password = input("Password: ")

    street = input("Street: ")
    number = input("Number: ")
    neighborhood = input("Neighborhood: ")
    city = input("City: ")
    state = input("State: ")
    adress = {  # not a json, it's a value-key
        "street": street,
        "number": number,
        "neighborhood": neighborhood,
        "city": city,
        "state": state,
    }
    mydoc = {"name": name, "email": email, "password": password, "adress": adress}
    insert = mycol.insert_one(mydoc)
    print("Document inserted with ID ", insert.inserted_id)
    print(" ")


def Delete_user(email):
    global db
    mycol = db.users
    myquery = {"email": email}
    mydoc = mycol.delete_one(myquery)
    print("User deleted! ")
    print(" ")


def Read_user(email):
    global db
    mycol = db.users
    print(" ")
    print("Found User: ")

    myquery = {"email": email}
    mydoc = mycol.find(myquery)
    for usr in mydoc:
        print(usr)


def Update_user(email):
    global db
    mycol = db.users
    myquery = {"email": email}
    mydoc = mycol.find_one(myquery)
    print("User data: ", mydoc)

    name = input("Change name:")
    if len(name):
        mydoc["name"] = name

    email = input("Change email:")
    if len(email):
        mydoc["email"] = email

    password = input("Change password:")
    if len(password):
        mydoc["password"] = password

    adress = {}
    street = input("Change Street: ")
    number = input("Change Number: ")
    neighborhood = input("Change Neighborhood: ")
    city = input("Change City: ")
    state = input("Change State: ")
    adress = {  # not a json, it's a value-key
        "street": street,
        "number": number,
        "neighborhood": neighborhood,
        "city": city,
        "state": state,
    }
    if len(adress):
        mydoc["adress"] = adress

    newvalues = {"$set": mydoc}
    mycol.update_one(myquery, newvalues)
    print(" ")


def Read_all_users():
    global db
    mycol = db.users
    print(" ")
    print("Existent users: ")
    mydoc = mycol.find().sort("name")
    for usr in mydoc:
        print("Name: ", usr["name"], "Email: ", usr["email"])
