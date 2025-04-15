import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('./app.db')  # Указание пути к твоей базе данных
cursor = conn.cursor()

# Запрос всех данных из таблицы product
cursor.execute("SELECT * FROM product")

# Получаем все строки
rows = cursor.fetchall()

# Печатаем каждую строку
for row in rows:
    print(row)  # или распечатывай по элементам row[0], row[1], и т.д.

# Закрытие соединения с базой данных
conn.close()
