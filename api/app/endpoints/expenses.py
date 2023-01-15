from contextlib import closing

from flask import jsonify
from flask_api import status

from database.Connection import get_connection

def get_first_record() -> dict:
    try:
        with closing(get_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                query = "SELECT * FROM expenses LIMIT 1"
                cursor.execute(query)

                row = cursor.fetchone()

                return {"message": f"Connection test OK: {row}"}
    except Exception as ex:
        return {"message": f"Failed to create connection! {ex}"}

def get_expenses_by_year(year):
    expenses = []
    try:
        with closing(get_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                query = f"SELECT * FROM expenses \
                WHERE YEAR(date) = '{year}';"
                cursor.execute(query)

                results = cursor.fetchall()
                for expense in results:
                    expenses.append({
                        "id": expense[0],
                        "description": expense[1],
                        "source": expense[2],
                        "date": expense[3],
                        "amount": expense[4],
                    })

                return jsonify(expenses), status.HTTP_200_OK
    except Exception as ex:
        return {"message": f"Failed to create connection! {ex}"}
