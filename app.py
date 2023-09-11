# app.py
from flask import Flask, render_template, request, jsonify
from helpers import greet, square

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet_route():
    data = request.get_json()
    name = data.get('name', 'Guest')
    greeting = greet(name)
    return jsonify({"greeting": greeting})

@app.route('/square', methods=['POST'])
def square_route():
    data = request.get_json()
    number = data.get('number', 0)
    result = square(number)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
