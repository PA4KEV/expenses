from contextlib import closing
from flask_api import FlaskAPI, status, request

from database.Connection import get_connection

app = FlaskAPI(__name__)

@app.route("/")
def hello():
    return {"message": "Hello, World!"}


@app.route("/connection_test")
def connection_test():
    try:
        with closing(get_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                query = "SELECT * FROM expenses LIMIT 1"
                cursor.execute(query)
                row = cursor.fetchone()
                return {"message": f"Connection test OK: {row}"}
    except Exception as ex:
        return {"message": f"Failed to create connection! {ex}"}



@app.route("/add", methods=["POST"])
def add():
    data = request.data
    x = data["x"]
    y = data["y"]
    result = x + y
    return {"result": result}, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
