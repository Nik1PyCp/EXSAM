from tkinter import *
import sqlite3

window = Tk()
window.title('products')
window.geometry('200x300')
window.config(bg='#3b3b3b')
inputAction = ''
connection = sqlite3.connect('products.sl3', 5)
cur = connection.cursor()
#cur.execute('CREATE TABLE products (name TEXT, price TEXT, number TEXT)')
#connection.commit()

def products(action):
      global inputAction
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
      if action == '1' or action == '2' or action == '3' or action == '4' or action == '5':
            inputAction = action
      if inputAction =='3':
            name = input('Enter name')
            price = int(input('Enter price'))
            number = int(input('Enter number'))
            print('OK it is create')
            cur.execute(f'INSERT INTO products (name, price, number) VALUES ("{name}" , "{price}" , "{number}")')
            connection.commit()
      if inputAction =='2':
            r1 = int(input('Enter row'))
            cur.execute(f'DELETE FROM products WHERE rowid = {r1}')
            connection.commit()
      if inputAction == '1':
            print(res)
      if inputAction == '4':
            name1 = input('Enter name')
            r2 = int(input('Enter row'))
            cur.execute(f'UPDATE products SET name = "{name1}" WHERE rowid = {r2}')
            connection.commit()
      if inputAction == '5':
            price1 = int(input('Enter price'))
            r3 = int(input('Enter row'))
            cur.execute(f'UPDATE products SET price = "{price1}" WHERE rowid = "{r3}"')
            connection.commit()

button = Button(text='1', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:products('1'))
button.grid(row=1, column=1)
button = Button(text='2', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:products('2'))
button.grid(row=1, column=2)
button = Button(text='3', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:products('3'))
button.grid(row=2, column=1)
button = Button(text='4', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:products('4'))
button.grid(row=2, column=2)
button = Button(text='5', font='Arial 15', fg='white', bg='#a6a6a6', relief=FLAT, width=2, height=2, command=lambda:products('5'))
button.grid(row=3, column=1)

cur.execute(f'SELECT rowid "name =" , name, "price=" , price, "number =" ,number FROM products')
connection.commit()
res = cur.fetchall()

label = Label(text=res, font='Arial 10', fg='red')
label.grid(columnspan=4)

window.mainloop()

