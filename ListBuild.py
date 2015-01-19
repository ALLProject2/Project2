import urllib2
import json

FPurl = "http://dev.c0l.in:5984/income_statements/_all_docs"
response = urllib2.urlopen(FPurl).read()
data= json.loads(response)

for item in data['rows']:
    print item['key']

    import urllib2
    import json

    FPurl2 = "http://dev.c0l.in:5984/income_statements/"
    response2 = urllib2.urlopen(FPurl2+item['key']).read()
    data2= json.loads(response)
    print data2
    

    


