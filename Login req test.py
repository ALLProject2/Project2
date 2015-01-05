username1 = "simran"
password1 = "password"


user1 = username1 + " "  + password1

reset = 1
while reset == 1:
    userinput = raw_input("Enter username followed by password:")

    if userinput == user1:
        print "login successful"
        reset = 0
        break
    else:
        reset = 1
        print "Your username or password is incorrect"
        
