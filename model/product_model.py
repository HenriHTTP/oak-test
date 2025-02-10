from database.connect import Databases


class Product(Databases):
    def __init__(self, name: str, description: str, price: float, is_available: bool):
        self.name = name
        self.description = description
        self.price = price
        self.is_available = is_available
