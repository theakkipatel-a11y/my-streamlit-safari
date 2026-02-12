import sqlite3

DB_NAME = "store.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products 
                 (id INTEGER PRIMARY KEY, name TEXT, price REAL, description TEXT, image_url TEXT)''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    data = c.fetchall()
    conn.close()
    return data

def add_product(name, price, desc, img):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO products (name, price, description, image_url) VALUES (?,?,?,?)", 
              (name, price, desc, img))
    conn.commit()
    conn.close()