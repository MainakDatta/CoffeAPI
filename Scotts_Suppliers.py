import requests
import json
from flask import Flask

app = Flask(__name__)
coffeenet = "http://coffee-net.azurewebsites.net/api/catalog/coffee"
hawaiiboom = "http://coffee-hawaii-boom.azurewebsites.net/api/v1.0/coffees"

def callSupplier(supplierURL):
	r = requests.get(coffeenet)
	return r.json()

def mergeCatalogs(catalog1, catalog2):
	result = []
	result.append(catalog1)
	result.append(catalog2)
	return result

@app.route('/')
def index():
	return "Hello World"

@app.route('/api/v1.0/catalog')
def catalog():
	supplier1 = callSupplier(coffeenet)
	supplier2 = callSupplier(hawaiiboom)
	mergedCatalogs = mergeCatalogs(supplier1,supplier2)
	return json.dumps(mergedCatalogs)

if __name__ == '__main__':
	app.run(debug=True)