from datetime import datetime

from flask_api import FlaskAPI, status, request

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
    # data = request.data
    # x = data["x"]
    # y = data["y"]
    return endpoints.expenses.set_expense(
        'Test description',
        'Test Source',
        12.34,
        datetime.strptime("2023-01-15 10:09:25", "%Y-%m-%d %H:%M:%S")
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
