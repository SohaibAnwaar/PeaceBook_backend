
from db_connection import get_connection

def create_user(username, user_password, email):
    try:
        cursor, connection = get_connection()
        cursor.execute("insert into users (username, user_password, email) values (%s,%s,%s)",(username, user_password, email))
        connection.commit()
        return "success"
    except Exception as e:
        print(f"[ERROR] - {e}")
        return "fail"
