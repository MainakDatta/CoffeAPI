import requests

def parseCoffeeNetToScotts(jsonData):
    ScottsCatalog = []
    newItem = {}
    for item in jsonData:
        newItem['name'] = item['description']
        newItem['description'] = item['tastingNotes']
        newItem['size'] = item['pricingData'][0]['size']
        newItem['price'] = item['pricingData'][0]['cost']
        newItem['quantity'] = item['pricingData'][0]['inStock']
        newItem['fairTrade'] = ""
        newItem['origin'] = ""
        newItem['grind'] = ""
        ScottsCatalog.append(newItem)


    return ScottsCatalog

def callSupplier(supplierURL):
	r = requests.get(supplierURL)
	return r.json()


coffeenet = "http://coffee-net.azurewebsites.net/api/catalog/coffee"
newCatalog = parseCoffeeNetToScotts(callSupplier(coffeenet))
print newCatalog