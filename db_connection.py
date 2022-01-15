import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="159.223.129.8",
                                  port="5432",
                                  database="postgres")

def get_connection():
    cursor = connection.cursor()
    cursor.execute("select * from users")
    record = cursor.fetchone()
    print("User db ", record)
    return cursor, connection


