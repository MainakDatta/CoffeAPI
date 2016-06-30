import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"

@app.route('/api/v1.0/catalog')
def catalog():
	r = requests.get("http://coffee-net.azurewebsites.net/api/catalog")
	return r.text

if __name__ == '__main__':
	app.run(debug=True)