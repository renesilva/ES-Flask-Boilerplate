# %% Imports
import os

from dotenv import load_dotenv
import mysql.connector

load_dotenv()

# %% Connect to external MySQL database
mysqldb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)
mysql_cursor = mysqldb.cursor()
