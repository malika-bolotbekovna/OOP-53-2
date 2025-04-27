import sqlite3
connect = sqlite3.connect('Staffs.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS staffs(
        staffid INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL,
        age INTEGER NOT NULL,
        birthday VARCHAR(50) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS shifts(
        shiftid INTEGER PRIMARY KEY AUTOINCREMENT,
        staffid INTEGER,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        FOREIGN KEY (staffid) REFERENCES staffs(staffid)
    )
''')

connect.commit()

def add_staff(name, age, birthday):
    cursor.execute('INSERT INTO staffs(name, age, birthday) VALUES (?, ?, ?)',
    (name, age, birthday))
    connect.commit()

add_staff('malika', 30, '1994-01-01')
add_staff('islam', 40, '1984-05-15')
add_staff('john', 25, '1999-09-09')

def add_shift(staffid, start_time, end_time):
    cursor.execute('INSERT INTO shifts(staffid, start_time, end_time) VALUES (?, ?, ?)',
    (staffid, start_time, end_time))
    connect.commit()

add_shift(1, '09:00', '17:00')
add_shift(2, '10:00', '18:00')


def create_view():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS staff_shifts_view AS
    SELECT
        name,
        age,
        birthday,
        start_time,
        end_time
    FROM
        staffs  
    LEFT JOIN
        shifts
    ON
        staffs.staffid = shifts.staffid
    ''')
    connect.commit()

create_view()

def get_view():
    cursor.execute('''SELECT * FROM staff_shifts_view''')
    rows = cursor.fetchall()

    for i in rows:
        print(f'NAME: {i[0]}, AGE: {i[1]}, BIRTHDAY: {i[2]}, START_TIME: {i[3]}, END_TIME: {i[4]}')

get_view()