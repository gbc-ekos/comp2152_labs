import sqlite3
from contextlib import closing

db_path = 'sqlite3.db'
try:
    with closing(sqlite3.connect(db_path)) as conn:
        conn.row_factory = sqlite3.Row
        with closing(conn.cursor()) as cursor:
            try:
                query_1 = "select * from demo where id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                print("Name of rows with id > 14;")
                for row in rows:
                    print(row['name'])
            except Exception as e:
                print("Error executing query:", e)
            try:
                del_row = int(input("Enter the row ID threshold for deletion "))
                query_2 = "delete from demo where id < ?"
                cursor.execute(query_2, (del_row,))
                num_rows = cursor.rowcount
                print(f"Number of rows affected: {num_rows}.")
                conn.commit()
            except ValueError as e: print("Invalid ID entered:", e)
            except Exception as e: print("Error executing query:", e)
except sqlite3.Error as e:
    print("Database connection error: ", e)

# TODO: with tracked files main.py and sqlite3.db
# TODO: commit into branch lab_week10
# TODO: merge lab_week10 into master
