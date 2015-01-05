def financial_statement():  #define code for financial statement as function
    import urllib2
    import json

    url = "http://dev.c0l.in:5984/financial_positions/30e901a7b7d8e98328dcd77c3600fa43"

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
        
    print("1. Non current assets") #print option 1
    print("2. Current assets") #print option 2
    print("3. Total assets") #print option 3
    print("4. Equity") #print option 4
    print("5. Non current liabilities") #print option 5
    print("6. Current liabilities") #print option 6
    print("7. Total equity and liabilities") #print option 7
    print("8. View ALL DATA") #print option 8
    print("9. Export without viewing") #print option 9

    num = input("Enter number:") #define user input selection

    if num == 1:    #if user selects option 1
        print ("non current assets are:"), non_current_assets   #print value
    elif num == 2:  #if user selects option 2
        print ("current assets are:"), current_assets   #print value
    elif num == 3:  #if user selects option 3
        print ("Total assets are:"), total_assets   #print value
    elif num == 4:  #if user selects option 4
        print ("Equity is:"), equity    #print value
    elif num == 5:  #if user selects option 5
        print ("non current liabilities are:"), non_current_liabilities     #print value
    elif num == 6:  #if user selects option 6
        print ("current liabilities are:"), current_liabilities     #print value
    elif num == 7:  #if user selects option 7
        print ("Total equity and liabilities are:"), total_equity_liabilities   #print value
    elif num == 8:  #if user selects option 8
        
        print ("non current assets are:"), non_current_assets       #print the result
        print ""    #print blank line

        print ("current assets are:"), current_assets       #print the result
        print ""    #print blank line

        print ("Total assets are:"), total_assets       #print the result
        print ""    #print blank line

        print ("Equity is:"), equity        #print the result
        print ""    #print blank line

        print ("non current liabilities are:"), non_current_liabilities         #print the result
        print ""    #print blank line

        print ("current liabilities are:"), current_liabilities     #print the result
        print ""    #print blank line

        print ("Total equity and liabilities are:"), total_equity_liabilities   #print the result
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
        
########Start System Main#############              
print ("1. Financial statement")    #display option 1
print ("2. Income statement")   #display option 2

selection = input("Enter number:")  #declare user selection variable

if selection == 1: #if user selects option 1
    financial_statement()   #call financial statement function




