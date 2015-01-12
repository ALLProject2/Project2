#Username and Password database

    #User = [Username, Password]

User1 = [["admin"], ["Password1"]]
User2 = [["simran"], ["Password2"]]
User3 = [["callum"], ["Password3"]]
User4 = [["cj"], ["Password4"]]
User5 = [["jamie"], ["Password5"]]
User6 = [["ben"], ["Password6"]]
User7 = [["guest"], ["Guest"]]

#Code

    #Existing Users
def existing():
    global lock1
    global lock2
    global Guest
    
    #Locks on access to program
    lock1 = "locked"
    lock2 = "locked"
    Iden = "User"
    Guest = False
    
    #Keeps the username lower case to avoid grammar issues
    Username = raw_input("Please enter your username  ").lower()

    #Checks Username input against database
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
    elif Username in User7[0]:
        lock1 = "unlocked"
        Iden = "Guest"
    else:
        lock1 = "locked"

    #Checks Password input against database
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
    elif Password in User7[1]:
        lock2 = "unlocked"
        Guest = True
    else:
        lock2 = "locked"

    #Action for locked program
    if lock1 == "locked":
        print "Incorrect Username"
    if lock2 == "locked":
        print "Incorrect Password"

    #Action for unlocked program
    if lock1 == "unlocked" and lock2 == "unlocked" and Guest == False:
        print "Welcome back " + Iden
    elif lock1 == "unlocked" and lock2 == "unlocked" and Guest == True:
        print "Welcome " + Iden
        print "Please note: Guests cannot export data"
        print "Please contact an administartor for a permanent login"

    #Non-registered users
def new():
    print("Please use our Guest Account ")
    print("Username: Guest")
    print("Password: Guest")
    print("Note: Password is Case Sensitive")
    print("")

    #Start menu
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
            
    #Launching program
Menu()
