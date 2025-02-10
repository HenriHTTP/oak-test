from database.connect import Databases
from repository.product_repository import ProductRepository
from model.product_model import Product
from view.product_view import ApplicationView

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

    Databases.close()
    ApplicationView()
