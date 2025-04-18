import sqlite3


# A4
connect = sqlite3.connect('Users.db')
# Рука с Ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD - Create - Read - Update - Delete

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )

    connect.commit()
    print(f'user is added: {name}')

# name = input('enter your name')

# add_user('john', 33, 'swim')

def get_all_user():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)

    if users:
        print('list of all users')
        for i in users:
            print(f'name: {i[0]}, age: {i[1]}, hobby: {i[2]}')
    else:
        print('list is empty')

# get_all_user()


def update_user_by_id(name, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, id)
    )

    connect.commit()
update_user_by_id('arzybek', 3)


def delete_user_by_id(id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (id, )
    )
    connect.commit()
    print('user is deleted')

# delete_user_by_id(2)