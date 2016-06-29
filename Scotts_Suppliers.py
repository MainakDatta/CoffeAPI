import requests
import json

r = requests.get("http://coffee-hawaii-boom.azurewebsites.net/api/v1.0/coffees")

print r.status_code
print ""
#j = json.loads(r.json())
#j = json.loads(r.text)
j = r.json()
print type(j[1])
print ""
print r.text
