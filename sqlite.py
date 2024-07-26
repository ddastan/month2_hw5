import sqlite3

try:
    # Подключение к базе данных (или создание, если ее не существует)
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

    print("Таблица успешно создана")

except sqlite3.Error as e:
    print(f"Ошибка создания таблицы. Сообщение от движка базы данных: {e}")
