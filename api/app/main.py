from datetime import datetime

from flask import request
from flask_api import FlaskAPI

import endpoints.expenses

app = FlaskAPI(__name__)

@app.route("/")
def hello():
    return {"message": "Hello, World!"}


@app.route("/connection_test")
def connection_test():
    return endpoints.expenses.get_first_record()


@app.route("/get_expenses/year/<int:year>", methods=["GET"])
def get_expenses_by_year(year):
    return endpoints.expenses.get_expenses_by_year(year)


@app.route("/insert_new_expense", methods=["POST"])
def insert_new_expense():
    description = request.form["description"]
    source = request.form["source"]
    amount = request.form["amount"]
    date = request.form["date"]
    time = request.form["time"]

    return endpoints.expenses.set_expense(
        description,
        source,
        float("{:.2f}".format(float(amount))),
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
