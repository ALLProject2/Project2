
############Financial Statement Main#######################
def financial_name_search():  #define code for financial statement as function

    user_response = raw_input("Type the business name to search" + " ")
    
    import urllib2
    import json

    
    FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"
    response = urllib2.urlopen(FPurl).read()
    data = json.loads(response)

    for item in data['rows']:
        FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']
        response2 = urllib2.urlopen(FPurl2).read()
        data2 = json.loads(response2)
        try:
            while user_response == data2['company']['name']:
            
                data_string = data2['company']['name'] + " " + data2['date'] + " " + data2['sector'] + " " + "ID:" + str(data2['id'])
                print data_string
                print "Seaching........."
                break
        except KeyError:
            print "All records retrieved!"
#financial_name_search()

    
import urllib2
import json

    
FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)

for item, data['id'] in sorted(data.items()):
    print(item, data['id'])


    
