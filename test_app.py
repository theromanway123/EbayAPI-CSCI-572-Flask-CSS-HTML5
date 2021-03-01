import requests
import json

url = "https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=RohanMar-EBAE-PRD-32eb49443-a134e220&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD"
r = requests.get(url)
print(type(r.json))
f = open('some.json','w')
json.dump(r.json(),f)
