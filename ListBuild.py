import urllib2
import json

FPurl = "http://dev.c0l.in:5984/income_statements/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)

for item in data['rows']:
    FPurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id']
    response2 = urllib2.urlopen(FPurl2).read()
    data2 = json.loads(response2)
    print data2['company']['name']
    


