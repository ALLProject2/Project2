def financial_statement():

    user_response = raw_input("Type the business name to search" + " ")
    
    import urllib2
    import json

    url = "http://dev.c0l.in:5984/financial_positions/_all_docs"

    response = urllib2.urlopen(url).read()
    data = json.loads(response.decode('utf8'))

    for item in data['rows']:
        url2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']

        response2 = urllib2.urlopen(url2).read()
        data2 = json.loads(response2.decode('utf8'))
        try:
            if user_response == data2['company']['name']:
                for items in data2['company']['name']:
            
                    data_string = data2['company']['name'] + " " + data2['date'] + " " + data2['sector']
                    print data_string
                    print "Seaching........."
                    counter =2
                    break
        except KeyError:
      
            print "All records retrieved!"

        
#financial_statement()

def financial_statement2():
    
    user_response = raw_input("Type the business name to search" + " ")
    user_response2 = raw_input("Enter the sector" + " ")
    user_response3 = raw_input("Enter the date" + " ")
    
    import urllib2
    import json

    url = "http://dev.c0l.in:5984/financial_positions/_all_docs"

    response = urllib2.urlopen(url).read()
    data = json.loads(response.decode('utf8'))

    for item in data['rows']:
        url2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']

        response2 = urllib2.urlopen(url2).read()
        data2 = json.loads(response2.decode('utf8'))
        try:
            if user_response == data2['company']['name'] and user_response2 == data2['sector'] and user_response3 == data2['date']:
                for items in data2['company']['name']:
            
                    data_string = data2['company']['name'] + " " + data2['date'] + " " + data2['sector']
                    print data_string
                    print "Seaching........."
                    counter =2
                    break
        except KeyError:
            
            print "All records retrieved!"


financial_statement2()




            
