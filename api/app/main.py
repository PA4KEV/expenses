from flask_api import FlaskAPI, status, request

app = FlaskAPI(__name__)

@app.route("/")
def hello():
    return {"message": "Hello, World!"}

@app.route("/add", methods=["POST"])
def add():
    data = request.data
    x = data["x"]
    y = data["y"]
    result = x + y
    return {"result": result}, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
