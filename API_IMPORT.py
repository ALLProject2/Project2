import urllib2
import json

url = "http://dev.c0l.in:5984/financial_positions/30e901a7b7d8e98328dcd77c3600fa43"

response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
#print data

#sort data into items
for key, value in data.iteritems():
    print key, value

#define non_current variable
non_current = float(data['company']['non_current_liabilities'])

#print non current liabilities
print ("Non current liabilities"), non_current


#Total Assets = Non current Assets + Current Assets

Assets_non_current = float(data['company']['non_current_assets'])

Assets_current = float(data['company']['current_assets'])

totalAssets = Assets_non_current + Assets_current

print ("Total assets are"), totalAssets
