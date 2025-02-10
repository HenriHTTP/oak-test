from database.connect import Databases
from model.product_model import Product


class ProductRepository(Databases):
    @classmethod
    def create_table(cls):
        cls.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                is_available BOOLEAN NOT NULL CHECK (is_available IN (0, 1))
            )
            """
        )
        cls.conn.commit()

    @classmethod
    def add_product(cls, product: Product):
        query: str = "INSERT INTO products (name, description, price, is_available) VALUES (?, ?, ?, ?)"
        cls.cur.execute(query,(product.name, product.description, product.price, int(product.is_available)))
        cls.conn.commit()

    @classmethod
    def get_all_products(cls):
        cls.cur.execute("SELECT id, name, description, price, is_available FROM products")
        return cls.cur.fetchall()

    @classmethod
    def search_products(cls, name: str):
        query = """
            SELECT id, name, description, price, is_available
            FROM products
            WHERE name LIKE ?
        """
        cls.cur.execute(query, ("%" + name + "%",))
