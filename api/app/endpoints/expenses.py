from contextlib import closing
from datetime import datetime

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

                return expenses
    except Exception as ex:
        return {"message": f"Failed to create connection! {ex}"}

def set_expense(
    description: str,
    source: str,
    amount: float,
    datetime: datetime
    ):

    try:
        with closing(get_connection()) as conn:
            with closing(conn.cursor()) as cursor:
                query = f"INSERT INTO expenses \
                (description, source, amount, date) \
                VALUES \
                ('{description}', '{source}', {amount}, '{datetime.strftime('%Y-%m-%d %H:%M:%S')}')"
                cursor.execute(query)

                if cursor.rowcount > 0:
                    conn.commit()
                    return {"message": f"New expense inserted. Rows affected: {cursor.rowcount}"}
                else:
                    return {"message": f"Unable to insert new record!"}
    except Exception as ex:
        return {"message": f"Error when creating a new expense! {ex}"}
