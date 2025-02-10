import sqlite3


class Databases:
    conn = None
    cur = None

    @classmethod
    def init_connection(cls, db_file):
        cls.conn = sqlite3.connect(db_file)
        cls.cur = cls.conn.cursor()
        cls.conn.commit()

    @classmethod
    def get_connection(cls):
        return cls.conn

    @classmethod
    def get_cursor(cls):
        return cls.cur

    @classmethod
    def close(cls):
        if cls.conn:
            cls.conn.close()







# Exemplo de uso
if __name__ == "__main__":
    Databases.init_connection("products.db")
    ProductRepository.create_table()

    # Adicionando produtos
    ProductRepository.add_product(Product("Notebook", "Laptop Dell 16GB RAM", 4500.99, True))
    ProductRepository.add_product(Product("Mouse Gamer", "Mouse RGB com 6 botões", 150.50, True))
    ProductRepository.add_product(Product("Cadeira", "Cadeira ergonômica para escritório", 899.90, False))

    # Buscando todos os produtos
    all_products = ProductRepository.get_all_products()
    print("Todos os produtos:", all_products)

    # Buscando por nome
    search_results = ProductRepository.search_products("Mouse")
    print("Produtos encontrados:", search_results)

    Databases.close()
