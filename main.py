import sqlite3


p = input('Enter 1 for check\nEnter 2 for delete row\nEnter 3 for create\nEnter 4 for rename\nEnter 5 for new price\n')
connection = sqlite3.connect('products.sl3', 5)
cur = connection.cursor()
#cur.execute('CREATE TABLE products (name TEXT, price TEXT, number TEXT)')
#connection.commit()

