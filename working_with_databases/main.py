# imported sqlite3 module
import sqlite3

# created a connection to the database
db = sqlite3.connect("books-collection.db")

# created a cursor object
cursor = db.cursor()

# # created a table
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

#
cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")

# commit the changes
db.commit()