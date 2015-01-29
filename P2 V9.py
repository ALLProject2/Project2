###########financial position search#################
def financial_position_search():  #define code for financial statement as function
    #menu
    print "1. Search by business name"  #display option 1
    print "2. Search business from sector"  #display option 2
    print " "   #print blank line

    search_selection = input("Enter a number: ")    #declare option input for menu

    if search_selection == 1:   #if the user selects 1 from the menu
    
        user_response = raw_input("Type the business name to search:" + " ")  #ask for user input
    
        import urllib2  #import library
        import json     #import json

        if statement == 1:  #if the user has selected financial position from the main menu
            FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"  #set the api url to financial position
        elif statement == 2:   #if the user selected income statement
            FPurl = "http://dev.c0l.in:5984/income_statements/_all_docs"    #set the api url to income statement
        
        response = urllib2.urlopen(FPurl).read()    #delcare response: open, read url library
        data = json.loads(response)     #delcare data: read response
        counter = 0     #set counter variable to 0
        a = []  #delcare blank list
        for item in data['rows']:   #start loop for every record in data
            
            if statement == 1:  #if the user has selected financial position from the main menu
                FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']     #use financial position api and add on the id from the record
            elif statement ==2: #if the user selected income statement
                FPurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id'] #use income statement api and add on the id from the record

            response2 = urllib2.urlopen(FPurl2).read() #delcare response
            data2 = json.loads(response2)   #delcare data
            try:    #set try as when at the end of the list the key won't be found
                while user_response == data2['company']['name']:  #if the business name entered matches one in the api
                    if statement == 1:  #if the user selected financial position from the main menu
                        data_string = data2['sector'] + ", " + data2['company']['name'] + ", " + data2['date'] + ", " + "id:" + str(data2['id']) #set the string
                    elif statement == 2:    #if the user selected income statement from the main menu
                        data_string = data2['sector'] + ", " + data2['company']['name'] + ", " + str(data2['fiscal_year_beginning']) + ", " + "id:" + str(data2['id'])  #set the string
                    counter = counter + 1   #set counter to add one to count number of records found
                    print counter   #print the counter value to display record number found
                    a.append(data_string) #add the value of the variable data_string to the empty list before it changes
                    break
            except KeyError:    #when at the end of api list there will be a KeyError
                    print "All records retrieved!" #print response
                    print " "   #print blank line
                    print "Sorting retrieved records..." #print sorting prompt
                    print " " #print blank line
                    a.sort()    #sort the list in alphabetical order
          
                    for val in a:
                        print val

                    id_search_financial_position()  #run the id search
                    
    elif search_selection == 2:     #if the user selects search by sector
        print " "                   #
        print "Available sectors:"  #
        print " "                   #        
        print "utilities"           #           
        print "consumer goods"      #  ###print sector values###     
        print "healthcare"          #
        print "basic materials"     #
        print "services"            #
        print "technology"          #
        print "industry goods"      #
        print "financial"           #
        print " "   #print blank line

        
        sector_selection = raw_input("Enter a sector: ")    #ask for user input

        
        if sector_selection == "utilities":
            print "Searching for all business records in the UTILITIES industry"
        elif sector_selection == "consumer goods":
            print "Searching for all business records in the CONSUMER GOODS industry"
        elif sector_selection == "healthcare":
            print "Searching for all business records in the HEALTHCARE industry"
        elif sector_selection == "basic materials":
            print "Searching for all business records in the BASIC MATERIALS industry"
        elif sector_selection == "services":
            print "Searching for all business records in the SERVICES industry"
        elif sector_selection == "technology":
            print "Searching for all business records in the TECHNOLOGY industry"
        elif sector_selection == "industry goods":
            print "Searching for all business records in the INDUSTRY GOODS industry"
        elif sector_selection == "financial":
            print "Searching for all business records in the FINANCIAL industry"
        else:
            financial_position_search()
        
        import urllib2  #import library
        import json     #import json

        if statement == 1: #if the user selected financial position from the main menu
            FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs" #use financial statement api
        elif statement ==2:     #if the user selected the income statement from the main menu
            FPurl = "http://dev.c0l.in:5984/income_statements/_all_docs" #use the income statement api
        
        response = urllib2.urlopen(FPurl).read()    #delcare resonse variable
        data = json.loads(response) #delcare data variable
        counter = 0     #set counter variable value to 0
        a = []  #declare empty list
        for item in data['rows']:   #for each record in the api
            if statement == 1: #if the user selected financial position from the main menu
                FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id'] #use financial statement api with record id on the end 
            elif statement ==2:
                FPurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id'] #use income statenemt api with recprd id on the end
            
            response2 = urllib2.urlopen(FPurl2).read() #declare resonse
            data2 = json.loads(response2) #declare data
            try:
                while sector_selection == data2['sector']:  #start loop
                                                            #while the users sector selection matches one in the api record 
                    if statement ==1:  #if the user selected financial position from the menu
                        data_string = data2['company']['name'] + ", " + data2['date'] + ", " + "id:" + str(data2['id']) #declare data string variable
                    elif statement == 2:    #if the user selected income statement from the main menu
                        data_string = data2['sector'] + ", " + data2['company']['name'] + ", " + str(data2['fiscal_year_beginning']) + ", " + "id:" + str(data2['id']) #declare data string variable
                    counter = counter + 1 #add one to counter everytime a record matching criteria is found
                    print counter #print the counter value to represent the number of records found matching the criteria
                    a.append(data_string) #add the data string value to the list
                    break
            except KeyError: 
                print "All records retrieved!" #print response
                print " "   #print blank line

                a.sort() #sort list in alphabetical order

                for val in a:
                    print val

                id_search_financial_position()  #run the id search 
    
    else:
        print " "
        print "Invalid input"
        print "Please try again"
        print " "
        financial_position_search()
        
def id_search_financial_position():     #define id search function

    input_id = raw_input("Enter ID from the list displayed above:" + " ")   #ask for user to input id
    print "Searching......please wait....."
    import urllib2
    import json

    if statement == 1:
        FPurl3 = "http://dev.c0l.in:5984/financial_positions/_all_docs"
    else:
        FPurl3 = "http://dev.c0l.in:5984/income_statements/_all_docs"
        
    response3 = urllib2.urlopen(FPurl3).read()
    global data3
    data3 = json.loads(response3)

    for items in data3['rows']:

        if statement == 1:
            FPurl4 = "http://dev.c0l.in:5984/financial_positions/" + items['id']
        else:
            FPurl4 = "http://dev.c0l.in:5984/income_statements/" + items['id']

        response4 = urllib2.urlopen(FPurl4).read()
        global data4
        data4 = json.loads(response4)
        
        try:
            while input_id == str(data4['id']):
                global data_string2 

                if statement ==1:
                        data_string2 = data4['company']['name'] + ", " + data4['date'] + ", " + "id:" + str(data4['id'])
                elif statement == 2:
                        data_string2 = data4['sector'] + ", " + data4['company']['name'] + ", " + str(data4['fiscal_year_beginning']) + ", " + "id:" + str(data4['id'])
                
                print " " 
                print data_string2
                print " "
                print "Please wait..."

                if statement == 1:
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
                else:
                    #define sales variable
                    global sales
                    sales = float(data4['company']['sales'])
        
                    #define opening_stock variable
                    global opening_stock
                    opening_stock = float(data4['company']['opening_stock'])
        
                    #define purchases
                    global purchases
                    purchases = float(data4['company']['purchases'])
        
                    #define closing_stock
                    global closing_stock
                    closing_stock = float(data4['company']['closing_stock'])
   
                    #define expenses
                    global expenses
                    expenses = float(data4['company']['expenses'])

                    #define interest_payable
                    global interest_payable
                    interest_payable = float(data4['company']['interest_payable'])
        
                    #define interest_receivable
                    global interest_receivable
                    interest_receivable = float(data4['company']['interest_receivable'])

                    #define and calc cost_of_sales
                    global cost_of_sales
                    cost_of_sales = opening_stock + purchases - closing_stock

                    #define and calc gross profit
                    global gross_profit
                    gross_profit = sales - cost_of_sales

                    #define and calc net profit
                    global net_profit
                    net_profit = gross_profit - expenses

                    #define and calc profit for period
                    global profit_for_period
                    profit_for_period = net_profit - interest_payable + interest_receivable

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
    if statement == 1:          
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
            system_main()
        else:
            print "OK"
            financial_position_search()

    else:

        print " "
        print "=========================DISPLAY========================="
        print ""
        print ("Sales are:" " " "£"), sales   #print value
        print ""    #print blank
            
        print ("Purchases are:"  " " "£"), purchases       #print the result
        print ""    #print blank line

        print ("Closing Stock is:"  " " "£"), closing_stock       #print the result
        print ""    #print blank line

        print ("Cost of Sales are:"  " " "£"), cost_of_sales       #print the result
        print ""    #print blank line

        print ("Gross Profit is:"  " " "£"), gross_profit        #print the result
        print ""    #print blank line

        print ("Expenses are:"  " " "£"), expenses        #print the result
        print ""    #print blank line

        print ("Net Profit is:"  " " "£"), net_profit     #print the result
        print ""    #print blank line

        print ("Interest Payable is:"  " " "£"), interest_payable   #print the result
        print ""    #print blank line

        print ("Interest Receivable is:"  " " "£"), interest_receivable   #print the result
        print ""    #print blank line

        print ("Profit for the Period is:"  " " "£"), profit_for_period   #print the result
        print ""    #print blank line

        export_csv = raw_input("Do you want to export to CSV? Y/N" + " ")
        export_csv = export_csv.upper()
        if export_csv == "Y":
        
            #build list value for CSV export
            income_statement = [purchases, closing_stock, cost_of_sales, gross_profit, expenses, net_profit, interest_payable, interest_receivable, profit_for_period]
            #build title list for CSV export
            title_list = ["Purchases", "Closing Stock", "Cost of Sales", "Gross Profit", "Expenses", "Net Profit", "Interest Payable", "Interest Receivable", "Profit For The Period"]
            #build list for service name
            import csv
            resultFile = open("IncomeStatement"+name+".csv",'wb')
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerow(service_name)  #write first row as sector name
            wr.writerow(["Company Name: " + name])    #write company name row
            wr.writerow(title_list)     #Write second row as title_list values
            wr.writerow(income_statement)     #write third row as financial_position values
            print("Export successful")
            system_main()
        else:
            print "OK"
            financial_position_search()
        

########Start System Main#############              
def system_main():
    print ("1. Financial statement")    #display option 1
    print ("2. Income statement")   #display option 2
    print ("3. Shutdown")   #display option 3

    print(" ")
    selection = input("Enter number: ")  #declare user selection variable
    print (" ")

    global statement
    if selection == 1: #if user selects option 1
        statement = 1
        financial_position_search()   #call financial statement function
    elif selection == 2:    #if user selects 2
        statement = 2
        financial_position_search() #call income statement function
    elif selection == 3:
       quit()
    else:
        print("You have entered an invalid number")
        print "Please try again"
        print(" ")
        system_main()
        
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

    




