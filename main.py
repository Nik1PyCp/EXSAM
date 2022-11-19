import sqlite3



p = input('Enter 1 for check\nEnter 2 for delete row\nEnter 3 for create\nEnter 4 for rename\nEnter 5 for new price\n')
connection = sqlite3.connect('products.sl3', 5)
cur = connection.cursor()
#cur.execute('CREATE TABLE products (name TEXT, price TEXT, number TEXT)')
#connection.commit()

def pe():
      global name
      global name1
      global price
      global price1
      global number
      global r1
      global r2
      global r3
      global row
      global cur
      if p =='3':
            name = input('Enter name')
            price = int(input('Enter price'))
            number = int(input('Enter number'))
            print('OK it is create')
            cur.execute(f'INSERT INTO products (name, price, number) VALUES ("{name}" , "{price}" , "{number}")')
            connection.commit()
      if p =='2':
            r1 = int(input('Enter row'))
            cur.execute(f'DELETE FROM products WHERE rowid = {r1}')
            connection.commit()
      if p == '1':
            print(res)
      if p == '4':
            name1 = input('Enter name')
            r2 = int(input('Enter row'))
            cur.execute(f'UPDATE products SET name = "{name1}" WHERE rowid = {r2}')
            connection.commit()
      if p == '5':
            price1 = int(input('Enter price'))
            r3 = int(input('Enter row'))
            cur.execute(f'UPDATE products SET price = "{price1}" WHERE rowid = "{r3}"')
            connection.commit()


cur.execute('SELECT rowid, name, price, number FROM products')
connection.commit()
res = cur.fetchall()
pe()

connection.close()
