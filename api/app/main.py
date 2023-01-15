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
def get_expenses(year):
    return endpoints.expenses.get_expenses_by_year(year)


@app.route("/add", methods=["POST"])
def add():
    data = request.data
    x = data["x"]
    y = data["y"]
    result = x + y
    return {"result": result}, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
