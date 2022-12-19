import sqlite3

def new_users():

    user = input("Введите логин пользователя: ")
    passwor = input("Введите пароль: ")
    status = input("Это Ученик или Учитель: ")

    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = """INSERT INTO 'users'
                                 (name, pass, status)
                                 VALUES (?, ?, ?);"""

        data_base = (user, passwor, status)
        cursor.execute(sqlite_insert_query, data_base)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def seach_users(name, passw):
    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()
        sql_select_query = """select * from users where name = ? and pass = ?"""
        cursor.execute(sql_select_query, (name, passw))
        records = cursor.fetchone()
        
        if records == None:
            print("Вы ввели неверно логин или пароль. Возможно такой пользователь не существует...")

        cursor.close()
        
        return records
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def delete_users(records):
    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()
        sql_delete_query = """DELETE from users where name = ? and pass = ?"""
        cursor.execute(sql_delete_query, (records[0], records[1]))
        sqlite_connection.commit()
        print("Пользователь успешно удален")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def all_users(param):
    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()
        if param == 'All':
            sql_select_query = """select * from users"""
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for i in records:
                print(i)
                
        else:
            sql_select_query = """select * from users where status = ?"""
            cursor.execute(sql_select_query, (param, ))
            records = cursor.fetchall()
            for i in records:
                print(i[0], i[2])

        cursor.close()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def add_home_work():
    lesson  = input("Введите тему урока: ")
    home = input("Введите дз: ")

    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = """INSERT INTO 'time_table'
                                 (lesson, home)
                                 VALUES (?, ?);"""

        data_base = (lesson, home)
        cursor.execute(sqlite_insert_query, data_base)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def time_table():
    try:
        sqlite_connection = sqlite3.connect('base.db')
        cursor = sqlite_connection.cursor()
        sql_select_query = """select * from time_table"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

        for i in records:
            print(i)
                
        cursor.close()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()