import urllib2
import json

url = "http://dev.c0l.in:5984/financial_positions/30e901a7b7d8e98328dcd77c3600fa43"

response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
print data

######12/09/1995 CJ######
