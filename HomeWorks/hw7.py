import sqlite3
from tabulate import tabulate as t

connect = sqlite3.connect('client.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS client(
        name VARCHAR(20)  NOT NULL,
        age INTEGER NOT NULL,
        birthday VARCHAR(50) NOT NULL
    )
''')

connect.commit()

def add_client(name, age, birthday):
    cursor.execute(
        'INSERT INTO client(name, age, birthday) VALUES (?, ?, ?)',
        (name, age, birthday)
    )
    connect.commit()

# for i in range(3):
#     name = input(f'\n{i + 1}. enter your name: ')
#     age = input('enter your age: ')
#     birthday = input('enter your birthday(exmpl: 10-june): ')
#     print('client is successfully added')
#     add_client(name, age, birthday)


def get_all_clients():
    cursor.execute('SELECT * FROM client')
    clients = cursor.fetchall()
    if clients:
        headers = ['Name', 'Age', 'Birthday']
        print('list of all clients')
        print(t(clients, headers=headers, tablefmt='grid'))
    else:
        print('list is empty')

# get_all_clients()


def update_client_by_id(name, id):
    cursor.execute(
        'UPDATE client SET name = ? WHERE rowid = ?',
        (name, id)
    )

    connect.commit()
# update_client_by_id('iyman', 3)


def delete_client_by_id(id):
    cursor.execute(
        'DELETE FROM client WHERE rowid = ?',
        (id, )
    )
    connect.commit()
    print('client is deleted')

# delete_client_by_id(1)