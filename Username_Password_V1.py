#Username and Password database

#User = [Username, Password]

User1 = [["admin"], ["Password1"]]
User2 = [["simran"], ["Password2"]]
User3 = [["callum"], ["Password3"]]
User4 = [["cj"], ["Password4"]]
User5 = [["jamie"], ["Password5"]]
User6 = [["ben"], ["Password6"]]

#Users = [["Admin", "Password1"], ["Simran", "Password2"], ["Callum", "Password3"], ["CJ", "Password4"], ["Jamie", "Password5"], ["Ben", "Password6"]]

def existing():
    global lock1
    global lock2
    lock1 = "locked"
    lock2 = "locked"
    Iden = "User"
    Username = raw_input("Please enter your username  ").lower()
    if Username in User1[0]:
        lock1 = "unlocked"
        Iden = "Admin"
    elif Username in User2[0]:
        lock1 = "unlocked"
        Iden = "Simran"
    elif Username in User3[0]:
        lock1 = "unlocked"
        Iden = "Callum"
    elif Username in User4[0]:
        lock1 = "unlocked"
        Iden = "CJ"
    elif Username in User5[0]:
        lock1 = "unlocked"
        Iden = "Jamie"
    elif Username in User6[0]:
        lock1 = "unlocked"
        Iden = "Ben"
    else:
        lock1 = "locked"
    
    Password = raw_input("Please enter your password  ")
    if Password in User1[1]:
        lock2 = "unlocked"
    elif Password in User2[1]:
        lock2 = "unlocked"
    elif Password in User3[1]:
        lock2 = "unlocked"
    elif Password in User4[1]:
        lock2 = "unlocked"
    elif Password in User5[1]:
        lock2 = "unlocked"
    elif Password in User6[1]:
        lock2 = "unlocked"
    else:
        lock2 = "locked"

    if lock1 == "locked":
        print "Incorrect Username"
    if lock2 == "locked":
        print "Incorrect Password"

    if lock1 == "unlocked" and lock2 == "unlocked":
        print "Welcome back " + Iden

def new():
    print("Please contact your system administrator to gain access ")
    print("")
    
def Menu():
    repeat = 1
    while repeat == 1:
        check = raw_input("Welcome, are you registered with this software? y/n  ").lower()
        if check == "y":
            existing()
            repeat = 0
        elif check == "n":
            new()
            repeat = 1
        else:
            print("Please answer y/n ")
            print("")
            repeat = 1

Menu()
