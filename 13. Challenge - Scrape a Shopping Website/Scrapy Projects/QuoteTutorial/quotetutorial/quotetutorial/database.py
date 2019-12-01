import sqlite3

conn = sqlite3.connect('myquotes.db') # Connection

# Ctrl + Shift + F10 to Run the file

curr = conn.cursor() # Cursor

# There are five types of storage classes : NULL, INTEGER, REAL, TEXT, BLOB.
# curr.execute("""create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text
#                 )""")

conn.execute("""insert into quotes_tb values('Python is awesome !!!','buildwithpython','python')""")

conn.commit()
conn.close()

# ctrl + shift +f10