#!/usr/bin/python3
"""
Starts a Flask Web Application
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""Return welcome message"""
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""Returns string hbnb"""
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
	"""Returns string c followed by any text"""

	return "C " + text.replace('_',' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
	"""Returns python followed by any string"""
	return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
