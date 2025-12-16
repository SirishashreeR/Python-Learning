import hashlib

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sirisha636@"
)

if conn.is_connected():
    print("Connected to MySQL")

cursor = conn.cursor()
cursor.execute("""
CREATE DATABASE IF NOT EXISTS first_db1
""")
conn.commit()

cursor.execute("USE first_db1")
print("Database selected")


cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    id INT,
    username VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100)
)
""")
conn.commit()

insert_query = """
INSERT INTO User (id, username, password)
VALUES (%s, %s, %s)
"""
password = "mypassword123"

hashed = hashlib.sha256(password.encode()).hexdigest()

data = (1, "supreeth",hashed)

cursor.execute(insert_query, data)
conn.commit()

print("Record inserted")



# create table tablename (username Varchar(200) PRIMARY KEY, password varchar(255));

# password = "mypassword123"

# hashed = hashlib.sha256(password.encode()).hexdigest()
# print(hashed)


