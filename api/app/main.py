from datetime import datetime

from flask import request, jsonify, make_response
from flask_api import FlaskAPI

import endpoints.expenses

app = FlaskAPI(__name__)

@app.route("/")
def hello():
    return {"message": "Hello, World!"}

@app.before_request
def before_request():
    app.logger.debug('BEFORE request')

    if request.method in ['OPTIONS']:
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

@app.route("/connection_test", methods=["GET"])
def connection_test():
    body = endpoints.expenses.get_first_record()

    response = make_response(jsonify(body))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    return response


@app.route("/get_expenses/year/<int:year>", methods=["GET"])
def get_expenses_by_year(year):
    body = endpoints.expenses.get_expenses_by_year(year)

    app.logger.debug('EXECUTE get expenses')

    response = make_response(jsonify(body))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    app.logger.debug('RETURN get expenses')

    return response


@app.route("/insert_new_expense", methods=["POST"])
def insert_new_expense():
    app.logger.debug('EXECUTE insert new expenses')

    data = request.get_json()
    description = data["expense"]["description"]
    source = data["expense"]["source"]
    amount = data["expense"]["amount"]
    date = data["expense"]["date"]
    time = data["expense"]["time"]

    body = endpoints.expenses.set_expense(
        description,
        source,
        float("{:.2f}".format(float(amount))),
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    )

    response = make_response(jsonify(body))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    app.logger.debug('RETURN insert new expenses')
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
