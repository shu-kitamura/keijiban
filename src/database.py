import os

import pyodbc
import dotenv

dotenv.load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")

def get_threads(thread_name):
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM thread WHERE name = ?", (thread_name,))
            return cursor.fetchall()

def get_posts(thread_id):
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM post WHERE thread_id = ?", (thread_id,))
            return cursor.fetchall()


for thread_row in get_threads("テストスレッド"):
    print("---" + str(thread_row[0]) + " " + str(thread_row[1]) + "---")
    for post_row in get_posts(thread_row[0]):
        print(str(post_row[0]) + " " + str(post_row[1]) + " " + str(post_row[2]) + " " + str(post_row[3]))

