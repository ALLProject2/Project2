import urllib2
import json

url = "http://dev.c0l.in:5984/financial_positions/30e901a7b7d8e98328dcd77c3600fa43"

response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
#sort data into items
for key, value in data.iteritems():
    print key, value
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
#define non_current_assets variable
non_current_assets = float(data['company']['non_current_assets'])
print ("non current assets are:"), non_current_assets       #print the result

print ""    #print blank line

#define current_assets variable
current_assets = float(data['company']['current_assets'])
print ("current assets are:"), current_assets       #print the result

print ""    #print blank line

#define and calculate total_assets
total_assets = non_current_assets + current_assets
print ("Total assets are:"), total_assets       #print the result

print ""    #print blank line

#define equity variable
equity = float(data['company']['equity'])
print ("Equity is:"), equity        #print the result

print ""    #print blank line

#define non_current_liabilities
non_current_liabilities = float(data['company']['non_current_liabilities'])
print ("non current liabilities are:"), non_current_liabilities         #print the result

print ""    #print blank line

#define current_liabilities
current_liabilities = float(data['company']['current_liabilities'])
print ("current liabilities are:"), current_liabilities     #print the result

print ""    #print blank line

#define and calculate total_equity_liabilities
total_equity_liabilities = equity + non_current_liabilities + current_liabilities
print ("Total equity and liabilities are:"), total_equity_liabilities   #print the result

print ""    #print blank line

#build list value for CSV export
financial_position = [non_current_assets, current_assets, total_assets, equity, non_current_liabilities, current_liabilities, total_equity_liabilities]
print financial_position    #print the list result

#build title list for CSV export
title_list = ["Non Current Assets", "Current Assets", "Total Assets", "Equity", "Non Current Liabilities", "Current Liabilities", "Total Equity and Liabilities"]

#build list for service name
service_name = ["Service Sector"]

#set-up CSV file
def exportCSV ():
    import csv
    resultFile = open("FinancialPosition.csv",'wb')
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(service_name)  #write first row as sector name 
    wr.writerow(title_list)     #Write second row as title_list values
    wr.writerow(financial_position)     #write third row as financial_position values


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
           






