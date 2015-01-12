############Financial Statement Main#######################
def financial_statement():  #define code for financial statement as function
    import urllib2
    import json
    user_input = raw_input("Enter 6 digit id: ")
    url = "http://dev.c0l.in:5984/financial_positions/30e901a7b7d8e98328dcd77c36" + user_input
    response = urllib2.urlopen(url).read()
    data = json.loads(response.decode('utf8'))

    
    #define non_current_assets variable
    global non_current_assets
    non_current_assets = float(data['company']['non_current_assets'])
        
    #define current_assets variable
    global current_assets
    current_assets = float(data['company']['current_assets'])
        
    #define and calculate total_assets
    global total_assets
    total_assets = non_current_assets + current_assets
        
    #define equity variable
    global equity
    equity = float(data['company']['equity'])
   
    #define non_current_liabilities
    global non_current_liabilities
    non_current_liabilities = float(data['company']['non_current_liabilities'])

    #define current_liabilities
    global current_liabilities
    current_liabilities = float(data['company']['current_liabilities'])
        
    #define and calculate total_equity_liabilities
    global total_equity_liabilities
    total_equity_liabilities = equity + non_current_liabilities + current_liabilities

    global name
    name = str(data['company']['name'])
    
    #set-up CSV file
    def exportCSV():
        #build list value for CSV export
        financial_position = [non_current_assets, current_assets, total_assets, equity, non_current_liabilities, current_liabilities, total_equity_liabilities]
        #build title list for CSV export
        title_list = ["Non Current Assets", "Current Assets", "Total Assets", "Equity", "Non Current Liabilities", "Current Liabilities", "Total Equity and Liabilities"]
        #build list for service name
        service_name = ["Service Sector"]
        import csv
        resultFile = open("FinancialPosition.csv",'wb')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(service_name)  #write first row as sector name 
        wr.writerow(title_list)     #Write second row as title_list values
        wr.writerow(financial_position)     #write third row as financial_position values
        print("Export successful")
    reset = 1
    while reset == 1:
        print(" ")
        print("Company Name: "),name
        print(" ")
        print("1. Non current assets") #print option 1
        print("2. Current assets") #print option 2
        print("3. Total assets") #print option 3
        print("4. Equity") #print option 4
        print("5. Non current liabilities") #print option 5
        print("6. Current liabilities") #print option 6
        print("7. Total equity and liabilities") #print option 7
        print("8. View ALL DATA") #print option 8
        print("9. Export without viewing") #print option 9
        print("10. Exit to previous menu") #print option 10

        print(" ")
        num = input("Enter number: ") #define user input selection
        
        if num == 1:    #if user selects option 1
            print ("non current assets are:" " " "£"), non_current_assets   #print value
            reset =1
        elif num == 2:  #if user selects option 2
            print ("current assets are:"  " " "£"), current_assets   #print value
            reset =1
        elif num == 3:  #if user selects option 3
            print ("Total assets are:" " " "£"), total_assets   #print value
            reset =1
        elif num == 4:  #if user selects option 4
            print ("Equity is:"  " " "£"), equity    #print value
            reset =1
        elif num == 5:  #if user selects option 5
            print ("non current liabilities are:"  " " "£"), non_current_liabilities     #print value
            reset =1
        elif num == 6:  #if user selects option 6
            print ("current liabilities are:"  " " "£"), current_liabilities     #print value
            reset =1
        elif num == 7:  #if user selects option 7
            print ("Total equity and liabilities are:"  " " "£"), total_equity_liabilities   #print value
            reset =1
        elif num == 8:  #if user selects option 8
            
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
           
            #ask user if CSV export is required
            x = True    #declare x variable    
            while x == True:        #setup loop
                user_input = raw_input("Would you like to export data to CSV? (Y/N)")   #declare user_input variable
                user_input = user_input.upper() #Convert user input to uppercase

                if user_input == "Y":   #if the user selects "Y"
                    exportCSV()     #run the export function
                    x == False      #change x variable to false
                    break           #exit
                elif user_input == "N":     #if the user selects "N"
                    print ("OK")        #print
                    x == False      #change x variable  
                    break       #exit
                else:               #if the user enters anything outside above parameters
                    print "You have entered an invalid input"
                    x == True       
        elif num == 9:
            exportCSV()
            reset =0
            break
        elif num == 10:
            def restart_main():
                print ("1. Financial statement")    #display option 1
                print ("2. Income statement")   #display option 2
                print ("3. Shutdown")   #display option 3

                print(" ")
                selection = input("Enter number:")  #declare user selection variable
                print (" ")

                if selection == 1: #if user selects option 1
                    financial_statement()   #call financial statement function
                elif selection == 2:
                    income_statement()
                elif selection == 3:
                    quit()
                else:
                    print("You have entered an invalid number")
                    print(" ")
            reset = 0
            restart_main()
            break
        else:
            print(" ")
            print "You have entered an ivalid number"
            reset = 1


############Income Statement Main##############
def income_statement():  #define code for income statement as function
    import urllib2
    import json

    user_input = raw_input("Enter 6 digit id: ")
    url = "http://dev.c0l.in:5984/income_statements/30e901a7b7d8e98328dcd77c36" + user_input


    response = urllib2.urlopen(url).read()
    data = json.loads(response.decode('utf8'))

    
    #define sales variable
    global sales
    sales = float(data['company']['sales'])
        
    #define opening_stock variable
    global opening_stock
    opening_stock = float(data['company']['opening_stock'])
        
    #define purchases
    global purchases
    purchases = float(data['company']['purchases'])
        
    #define closing_stock
    global closing_stock
    closing_stock = float(data['company']['closing_stock'])
   
    #define expenses
    global expenses
    expenses = float(data['company']['expenses'])

    #define interest_payable
    global interest_payable
    interest_payable = float(data['company']['interest_payable'])
        
    #define interest_receivable
    global interest_receivable
    interest_receivable = float(data['company']['interest_receivable'])

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
    name = str(data['company']['name'])
                      

    #set-up CSV file
    def exportCSV():
        #build list value for CSV export
        income_statement = [purchases, closing_stock, cost_of_sales, gross_profit, expenses, net_profit, interest_payable, interest_receivable, profit_for_period]
        #build title list for CSV export
        title_list = ["Purchases", "Closing Stock", "Cost of Sales", "Gross Profit", "Expenses", "Net Profit", "Interest Payable", "Interest Receivable", "Profit For The Period"]
        #build list for service name
        service_name = ["Service Sector"]
        import csv
        resultFile = open("IncomeStatement.csv",'wb')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(service_name)  #write first row as sector name 
        wr.writerow(title_list)     #Write second row as title_list values
        wr.writerow(income_statement)     #write third row as financial_position values
        print("Export successful")
    reset = 1
    while reset == 1:
        print ""
        print ("Company Name:" ""), name
        print(" ")
        print("1. Sales")   #print option 1
        print("2. Purchases") #print option 2
        print("3. Closing Stock") #print option 3
        print("4. Cost of Sales") #print option 4
        print("5. Gross Profit") #print option 5
        print("6. Expenses") #print option 6
        print("7. Net Profit") #print option 7
        print("8. Interest Payable") #print option 8
        print("9. Interest Receivable") #print option 9
        print("10. Profit For The Period") #print option 10
        print("11. View ALL DATA") #print option 11
        print("12. Export without viewing") #print option 12
        print("13. Exit to previous menu") #print option 13

        print(" ")
        num = input("Enter number:") #define user input selection

        if num == 1:    #if user selects option 1
            print ("Sales are:" " " "£"), sales   #print value
            reset =1
        if num == 2:    #if user selects option 1
            print ("Purchases are:" " " "£"), purchases   #print value
            reset =1
        elif num == 3:  #if user selects option 2
            print ("Closing Stock is:"  " " "£"), closing_stock   #print value
            reset =1
        elif num == 4:  #if user selects option 3
            print ("Cost of Sales are:" " " "£"), cost_of_sales   #print value
            reset =1
        elif num == 5:  #if user selects option 4
            print ("Gross Profit is:"  " " "£"), gross_profit    #print value
            reset =1
        elif num == 6:  #if user selects option 5
            print ("Expenses are:"  " " "£"), expenses     #print value
            reset =1
        elif num == 7:  #if user selects option 6
            print ("Net Profit is:"  " " "£"), net_profit     #print value
            reset =1
        elif num == 8:  #if user selects option 7
            print ("Interest Payable is:"  " " "£"), interest_payable  #print value
            reset =1
        elif num == 9:  #if user selects option 8
            print ("Interest Receivable is:"  " " "£"), interest_receivable  #print value
            reset =1
        elif num == 10:  #if user selects option 9
            print ("Profit for the Period is:"  " " "£"), profit_for_period  #print value
            reset =1
        elif num == 11:  #if user selects option 10

            
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

            #ask user if CSV export is required
            x = True    #declare x variable    
            while x == True:        #setup loop
                user_input = raw_input("Would you like to export data to CSV? (Y/N)")   #declare user_input variable
                user_input = user_input.upper() #Convert user input to uppercase

                if user_input == "Y":   #if the user selects "Y"
                    exportCSV()     #run the export function
                    x == False      #change x variable to false
                    break           #exit
                elif user_input == "N":     #if the user selects "N"
                    print ("OK")        #print
                    x == False      #change x variable  
                    break       #exit
                else:               #if the user enters anything outside above parameters
                    print "You have entered an invalid input"
                    x == True       
        elif num == 12:
            exportCSV()
            reset =0
            break
        elif num == 13:
            def restart_main():
                print ("1. Financial statement")    #display option 1
                print ("2. Income statement")   #display option 2
                print ("3. Shutdown")   #display option 3

                print(" ")
                selection = input("Enter number:")  #declare user selection variable
                print (" ")

                if selection == 1: #if user selects option 1
                    financial_statement()   #call financial statement function
                elif selection == 2:    #if user selects 2
                    income_statement()  #call income statement function
                elif selection == 3:
                    quit()
                else:
                    print("You have entered an invalid number")
                    print(" ")
                    reset = 0
            restart_main()
                    
        else:
            print(" ")
            print "You have entered an invalid number"
            reset = 1
            break



            
########Start System Main#############              
def system_main():
    print ("1. Financial statement")    #display option 1
    print ("2. Income statement")   #display option 2
    print ("3. Shutdown")   #display option 3

    print(" ")
    selection = input("Enter number: ")  #declare user selection variable
    print (" ")

    if selection == 1: #if user selects option 1
        financial_statement()   #call financial statement function
    elif selection == 2:    #if user selects 2
        income_statement()  #call income statement function
    elif selection == 3:
       quit()
    else:
        print("You have entered an invalid number")
        print(" ")
        
system_main()
