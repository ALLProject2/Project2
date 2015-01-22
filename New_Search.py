def financial_statement():  #define code for financial statement as function

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
        if data2['company']['name'] == user_response:
            counter =1
            while counter ==1:
                print data2['company']['name'] + " " + data2['date'] + " " + data2['sector']
                print "Seaching........."
                counter ==2
                break
    print "All records retrieved"

financial_statement()
