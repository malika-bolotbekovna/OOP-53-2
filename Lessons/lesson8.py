import sqlite3
connect = sqlite3.connect('UsersGrades.db')
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        userid INTEGER PRIMARY KEY AUTOINCREMENT,-- Уникальный идентификатор пользователя
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS grades (
                    gradeid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор записи о оценке
                    userid INTEGER,                            -- Внешний ключ, который ссылается на userid из таблицы 'users'
                    subject VARCHAR(100) NOT NULL,             -- Название предмета
                    grade INTEGER NOT NULL,                    -- Оценка
                    FOREIGN KEY (userid) REFERENCES users(userid) -- Определяем связь с таблицей 'users'
                )
            ''')

connect.commit()


def add_user(name, age, hobby=""):
    cursor.execute('INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)', (name, age, hobby))
    connect.commit()
    print(f"Пользователь {name} добавлен")

# add_user('Илья Муромец', 25, 'фехтование')
# add_user('John Doe1', 25, 'плавание')
# add_user('John Doe2', 27, 'шахматы')
# add_user('John Doe3', 28, 'чтение')
# add_user('John Doe4', 35, 'шахматы')
# add_user('John Doe5', 33, 'чтение')



def add_user_grade(userid, subject, grade):
    cursor.execute('''INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)''',
                   (userid, subject, grade))
    connect.commit()

# add_user_grade(3, "Алгебра", 2)
# add_user_grade(4, "Геометрия", 1)
# add_user_grade(2, "Физика", 2)



def get_users_grade():
    cursor.execute('''
    SELECT users.name, grades.subject, grades.grade
    FROM users LEFT JOIN grades ON users.userid = grades.userid
    ''')

    rows = cursor.fetchall()

    print("Пользователи с их оценками (LEFT JOIN):")

    for i in rows:
        print(f"NAME: {i[0]}, SUBJECT: {i[1]}, GRADE: {i[2]}")

# get_users_grade()


# # AVG() – Среднее значение
# # MAX() – Максимальное значение
# # MIN() – Минимальное значение  COUNT() SUM()


# # Агрегационные функции и группировка данных

def get_avg_age():
    cursor.execute('SELECT AVG(age) FROM users')
    avg = cursor.fetchone()

    print(f"Средний возраст {avg}")

# get_avg_age()
# # Пердставления - VIEW

def create_view_young_user():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS young_users AS
    SELECT name, age
    FROM users WHERE age < 30
    ''')
    connect.commit()

# create_view_young_user()


def get_young_users():
    cursor.execute('SELECT * FROM young_users')
    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}")
# get_young_users()