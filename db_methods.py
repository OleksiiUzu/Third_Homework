import sqlite3


# Функцію я потім перероблю в класс як на занятті
def get_db_data(sql_command):
    try:
        connection = sqlite3.connect('Dishes.db')
        print("База даних підключена до SQLite.")
        cursor = connection.cursor()
        result = cursor.execute(sql_command)
        print("Скрипт SQLite успішно виконаний")
        data = result.fetchall()
        for i in data:
            print(i)
        return data
    except sqlite3.Error as error:
        print("Помилка при підключенні до SQLite.", error)
    finally:
        if connection:
            connection.close()
            print("З'єднання з SQLite закрито.")
