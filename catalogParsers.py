import requests

def parseCoffeeNetToScotts(jsonData):
    ScottsCatalog = []
    newItem = {}
    for item in jsonData:
        for priceData in item['pricingData']:
            newItem['name'] = item['description']
            newItem['description'] = item['tastingNotes']
            newItem['size'] = priceData['size']
            newItem['price'] = priceData['cost']
            newItem['quantity'] = priceData['inStock']
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