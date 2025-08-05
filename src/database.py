import os

import pyodbc
import dotenv

dotenv.load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")

def select_threads(thread_name) -> list[pyodbc.Row]:
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name FROM thread WHERE name LIKE ?", (f"%{thread_name}%",))
            return cursor.fetchall()

def select_posts(thread_id) -> list[pyodbc.Row]:
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT timestamp, content FROM post WHERE thread_id = ?", (thread_id,))
            return cursor.fetchall()

def insert_post(thread_id, content):
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO post (thread_id, content) VALUES (?, ?)", (thread_id, content))
            conn.commit()

def insert_thread(thread_name: str):
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO thread (name) VALUES (?)", (thread_name,))
            conn.commit()
