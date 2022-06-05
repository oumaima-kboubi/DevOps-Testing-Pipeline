import sqlite3
import os

def create_db(database_filename):
    # connect to SQLite
    con = sqlite3.connect(database_filename)

    # Create  a connection
    cursor = con.cursor()

    # Drop tasks table if already exists
    cursor.execute("DROP TABLE IF EXISTS tasks")

    # Create tasks table in db_web database
    sql = '''CREATE TABLE "tasks" (
        "task_id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "taskname" TEXT,
        "status" TEXT
    )'''
    cursor.execute(sql)

    # Commit changes
    con.commit()

    #Close connection
    con.close()
if __name__ == '__main__':
    database_filename = os.environ.get('DATBASE_FILENAME','oumatasks.db')
    create_db(database_filename)