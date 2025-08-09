"""
This module handles SELECT and INSERT to the database.
"""

import os

import pyodbc
import dotenv

from error import DBError, DBErrorKind

dotenv.load_dotenv()

def try_connect() -> pyodbc.Connection:
    """This function tries to connect to the database."""
    conn_str = os.getenv("CONNECTION_STRING")
    if not conn_str:
        raise DBError("connection string is not set.", DBErrorKind.ConnectionError)

    try:
        conn = pyodbc.connect(
            conn_str,
            timeout=15
        )
        return conn
    except pyodbc.Error as e:
        raise DBError(f"failed to connect to database.\n{e}", DBErrorKind.ConnectionError)

def select_threads(thread_name) -> list[pyodbc.Row]:
    """This function selects a thread from the database.

    It performs a partial match search using the thread name received as an argument.
    """
    try:
        with try_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name FROM thread WHERE name LIKE ?", (f"%{thread_name}%",))
                return cursor.fetchall()
    except DBError as e:
        raise e
    except pyodbc.Error as e:
        raise DBError(f"failed to select threads.\n{e}", DBErrorKind.QueryError)

def select_posts(thread_id) -> list[pyodbc.Row]:
    """This function selects posts from the database for a given thread ID."""
    try:
        with try_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT timestamp, content FROM post WHERE thread_id = ?", (thread_id,))
                return cursor.fetchall()
    except DBError as e:
        raise e
    except pyodbc.Error as e:
        raise DBError(f"failed to select posts.\n{e}", DBErrorKind.QueryError)

def insert_post(thread_id, content) -> None:
    """This function inserts a post into the database for a given thread ID."""
    try:
        with try_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO post (thread_id, content) VALUES (?, ?)", (thread_id, content))
                conn.commit()
    except DBError as e:
        raise e
    except pyodbc.Error as e:
        raise DBError(f"failed to insert post.\n{e}", DBErrorKind.QueryError)

def insert_thread(thread_name: str) -> str:
    """This function inserts a thread into the database.

    Returns the ID of the inserted thread.
    """
    try:
        with try_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO thread (name) OUTPUT INSERTED.id VALUES (?)", (thread_name,))
                id = cursor.fetchone()
                conn.commit()
                return id[0]
    except DBError as e:
        raise e
    except pyodbc.Error as e:
        raise DBError(f"failed to insert thread.\n{e}", DBErrorKind.QueryError)