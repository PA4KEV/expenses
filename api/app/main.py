from flask_api import FlaskAPI, status, request
import mysql.connector

app = FlaskAPI(__name__)


def create_connection():
    try:
        conn = mysql.connector.connect(
            host="exp_db",
            user="root",
            password="password",
            database="mydb"
        )

        return conn
    except mysql.connector.Error as e:
        return f"Error connecting to MariaDB: {e}"


@app.route("/")
def hello():
    return {"message": "Hello, World!"}


@app.route("/connect")
def connect():
    return {"message": f"Connection {create_connection()}"}

@app.route("/add", methods=["POST"])
def add():
    data = request.data
    x = data["x"]
    y = data["y"]
    result = x + y
    return {"result": result}, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
