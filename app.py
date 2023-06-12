from flask import Flask,request,jsonify
from flask_cors import CORS
from negocio.calculadora_neg import Calculadora
# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Hello world!'


@app.route('/sum', methods=['POST'])
def login():
    print("REQUEST: ", request.json)
    sum_object = request.json
    calc = Calculadora()
    sum = calc.suma(sum_object['sum1'],sum_object['sum1'])
    result = {}
    result["result"] = sum
    return jsonify(Suma=result), 200

@app.route('/subs', methods=['POST'])
def login():
    print("REQUEST: ", request.json)
    calc = Calculadora()
    resta = calc.suma(request.json['num1'],request.json['num2'])
    result = {}
    result["result"] = resta
    return jsonify(Resta=result), 200


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
