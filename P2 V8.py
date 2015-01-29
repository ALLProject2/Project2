###########financial position search#################
def financial_position_search():  #define code for financial statement as function

    print "1. Search by business name"
    print "2. Search business from sector"
    print " " 

    search_selection = input("Enter a number: ")

    if search_selection == 1:
    
        user_response = raw_input("Type the business name to search" + " ")     #ask for user input
    
        import urllib2  #import library
        import json     #import json

    
        FPurl = "http://dev.c0l.in:5984/income_statements/_all_docs"
        response = urllib2.urlopen(FPurl).read()
        data = json.loads(response)
        counter = 0
        a = []
        for item in data['rows']:
            FPurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id']
            response2 = urllib2.urlopen(FPurl2).read()
            data2 = json.loads(response2)
            try:
                while user_response == data2['company']['name']:
            
                    data_string = data2['sector'] + ", " + data2['company']['name'] + ", " + data2['date'] + ", " + "id:" + str(data2['id'])
                    counter = counter + 1
                    print counter
                    a.append(data_string)
                    break
            except KeyError:
                print "All records retrieved!"
                print " "
                print "Sorting retrieved records..."
                print " " 
                a.sort()
            

                value = 0
                try:
                    while value <= counter:
                        print a[value]
                        print " " 
                        value = value + 1
                except IndexError:
                    print "Done!"
                    print " "
                    id_search_financial_position()
                    
    elif search_selection == 2:
        print " " 
        print "Available sectors:"
        print " "
        print "utilities"
        print "consumer goods"
        print "healthcare"
        print "basic materials"
        print "services"
        print "technology"
        print "industry goods"
        print "financial"
        print " " 

    sector_selection = raw_input("Enter a sector: ")

    import urllib2  #import library
    import json     #import json

    
    FPurl = "http://dev.c0l.in:5984/income_statements/_all_docs"
    response = urllib2.urlopen(FPurl).read()
    data = json.loads(response)
    counter = 0
    a = []
    for item in data['rows']:
        FPurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id']
        response2 = urllib2.urlopen(FPurl2).read()
        data2 = json.loads(response2)
        try:
            while sector_selection == data2['sector']:
            
                data_string = data2['company']['name'] + ", " + data2['date'] + ", " + "id:" + str(data2['id'])
                counter = counter + 1
                print counter
                a.append(data_string)
                break
        except KeyError:
            print "All records retrieved!"
            print " "

            a.sort()
            

            value = 0
            try:
                while value <= counter:
                    print a[value]
                    print " " 
                    value = value + 1
            except IndexError:
                print "Done!"
                print " "
                #id_search_financial_position()    
    

def id_search_financial_position():

    input_id = raw_input("Enter ID from the list displayed above:" + " ")

    import urllib2
    import json

    
    FPurl3 = "http://dev.c0l.in:5984/income_statements/_all_docs"
    response3 = urllib2.urlopen(FPurl3).read()
    global data3
    data3 = json.loads(response3)

    for items in data3['rows']:
        FPurl4 = "http://dev.c0l.in:5984/income_statements/" + items['id']
        response4 = urllib2.urlopen(FPurl4).read()
        global data4
        data4 = json.loads(response4)
        try:
            while input_id == str(data4['id']):
                global data_string2 
                data_string2 = data4['sector'] + ", " + data4['company']['name'] + ", " + data4['date'] + ", " + "id:" + str(data4['id'])
                print " " 
                print data_string2

                #define non_current_assets variable
                global non_current_assets
                non_current_assets = float(data4['company']['non_current_assets'])
        
                #define current_assets variable
                global current_assets
                current_assets = float(data4['company']['current_assets'])
        
                #define and calculate total_assets
                global total_assets
                total_assets = non_current_assets + current_assets
        
                #define equity variable
                global equity
                equity = float(data4['company']['equity'])
   
                #define non_current_liabilities
                global non_current_liabilities
                non_current_liabilities = float(data4['company']['non_current_liabilities'])

                #define current_liabilities
                global current_liabilities
                current_liabilities = float(data4['company']['current_liabilities'])
        
                #define and calculate total_equity_liabilities
                global total_equity_liabilities
                total_equity_liabilities = equity + non_current_liabilities + current_liabilities

                #define name
                global name
                name = str(data4['company']['name'])

                #define sector
                global service_name
                service_name = data4['sector']
                
                break
        except KeyError:
            print " " 
            print "All records retrieved!"
            financial_statement_display()


def financial_statement_display():
              
    print" "
    print "=========================DISPLAY========================="
    print ("Financial position information for record:") , data_string2
    print " "

    print ("non current assets are:"  " " "£"), non_current_assets       #print the result
    print ""    #print blank line

    print ("current assets are:"  " " "£"), current_assets       #print the result
    print ""    #print blank line

    print ("Total assets are:"  " " "£"), total_assets       #print the result
    print ""    #print blank line

    print ("Equity is:"  " " "£"), equity        #print the result
    print ""    #print blank line

    print ("non current liabilities are:"  " " "£"), non_current_liabilities         #print the result
    print ""    #print blank line

    print ("current liabilities are:"  " " "£"), current_liabilities     #print the result
    print ""    #print blank line

    print ("Total equity and liabilities are:"  " " "£"), total_equity_liabilities   #print the result
    print ""    #print blank line

    export_csv = raw_input("Do you want to export to CSV? Y/N" + " ")
    export_csv = export_csv.upper()
    if export_csv == "Y":
        #build list value for CSV export
        financial_position = [non_current_assets, current_assets, total_assets, equity, non_current_liabilities, current_liabilities, total_equity_liabilities]
        #build title list for CSV export
        title_list = ["Non Current Assets", "Current Assets", "Total Assets", "Equity", "Non Current Liabilities", "Current Liabilities", "Total Equity and Liabilities"]
        import csv
        resultFile = open("FinancialPosition" + name +".csv",'wb')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(["Sector: " + service_name])  #write first row as sector name 
        wr.writerow(["Company Name: " + name])    #write company name row   
        wr.writerow(title_list)     #Write second row as title_list values
        wr.writerow(financial_position)     #write third row as financial_position values
        print("Export successful")
    else:
        print "OK"
        

########Start System Main#############              
def system_main():
    print ("1. Financial statement")    #display option 1
    print ("2. Income statement")   #display option 2
    print ("3. Shutdown")   #display option 3

    print(" ")
    selection = input("Enter number: ")  #declare user selection variable
    print (" ")

    if selection == 1: #if user selects option 1
        financial_position_search()   #call financial statement function
    elif selection == 2:    #if user selects 2
        income_statement()  #call income statement function
    elif selection == 3:
       quit()
    else:
        print("You have entered an invalid number")
        print(" ")
        
##########Login Req####################
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
    if lock1 == "locked" and lock2 == "locked":
        print "Incorrect Username"
        print "Incorrect Password"
        existing()
    elif lock1 == "locked":
        print "Incorrect Username"
        existing()
    elif lock2 == "locked":
        print "Incorrect Password"
        existing()

    #Action for unlocked program
    if lock1 == "unlocked" and lock2 == "unlocked" and Guest == False:
        print ""
        print "Welcome back " + Iden
        print ""
        system_main()
    elif lock1 == "unlocked" and lock2 == "unlocked" and Guest == True:
        print ""
        print "Welcome " + Iden
        print "Please contact an administartor for a permanent login"
        print ""
        system_main()

    #Non-registered users
def new():
    print("Please use our Guest Account ")
    print("Username: Guest")
    print("Password: Guest")
    print("Note: Password is Case Sensitive")
    print("")
    existing()

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

    




