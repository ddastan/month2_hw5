import sqlite3

def create_connection(db_file):
    """Создает подключение к базе данных SQLite"""
    conn = sqlite3.connect(db_file)
    return conn


conn = create_connection('hw.db')
cursor = conn.cursor()

def create_table():
    """Создает таблицу products"""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()

create_table()


def add_products():
    """Добавляет 15 различных товаров в таблицу products"""
    products = [
        ("Product1", 50.5, 10),
        ("Product2", 70.2, 5),
        ("Product3", 30.0, 20),
        # Добавьте еще 12 продуктов по аналогии
    ]

    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)
    ''', products)
    conn.commit()


add_products()
def update_quantity(product_id, new_quantity):
    """Изменяет количество товара по id"""
    cursor.execute('''
    UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

update_quantity(1, 15)
def update_price(product_id, new_price):
    """Изменяет цену товара по id"""
    cursor.execute('''
    UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

update_price(1, 60.0)
def delete_product(product_id):
    """Удаляет товар по id"""
    cursor.execute('''
    DELETE FROM products WHERE id = ?
    ''', (product_id,))
    conn.commit()

delete_product(1)
def print_all_products():
    """Выбирает все товары из БД и распечатывает их в консоли"""
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

print_all_products()
def print_products_below_limit(price_limit, quantity_limit):
    """Выбирает товары дешевле определенной цены и с количеством больше лимита"""
    cursor.execute('''
    SELECT * FROM products WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

print_products_below_limit(100, 5)
def search_products_by_title(search_term):
    """Ищет товары по названию"""
    cursor.execute('''
    SELECT * FROM products WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

search_products_by_title("мыло")
conn.close()
