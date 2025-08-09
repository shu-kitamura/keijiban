"""
This module handles SELECT and INSERT to the database.
"""

import os

import pyodbc
import dotenv

dotenv.load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")

def select_threads(thread_name) -> list[pyodbc.Row]:
    """This function selects a thread from the database.

    It performs a partial match search using the thread name received as an argument.
    """
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name FROM thread WHERE name LIKE ?", (f"%{thread_name}%",))
            return cursor.fetchall()

def select_posts(thread_id) -> list[pyodbc.Row]:
    """This function selects posts from the database for a given thread ID."""
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT timestamp, content FROM post WHERE thread_id = ?", (thread_id,))
            return cursor.fetchall()

def insert_post(thread_id, content) -> None:
    """This function inserts a post into the database for a given thread ID."""
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO post (thread_id, content) VALUES (?, ?)", (thread_id, content))
            conn.commit()

def insert_thread(thread_name: str) -> str:
    """This function inserts a thread into the database.

    Returns the ID of the inserted thread.
    """
    with pyodbc.connect(CONNECTION_STRING) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO thread (name) OUTPUT INSERTED.id VALUES (?)", (thread_name,))
            id = cursor.fetchone()
            conn.commit()

    return id[0]
