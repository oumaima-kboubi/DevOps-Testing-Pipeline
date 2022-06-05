import os
import sqlite3
from flask import Flask


app = Flask(__name__)
database_filename =  os.environ.get('DATABASE_FILENAME','oumatasks.db')
db_connection = sqlite3.connect(database_filename, check_same_thread=False)

app.config.from_mapping(
    DATABASE_CON=db_connection
)
from app import routes