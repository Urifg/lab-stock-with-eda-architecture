class Product:
    def __init__(self, sku: str, name: str):
        self.sku = sku
        self.name: str = name

    def __repr__(self):
        return f"<Product {self.sku}>"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return other.sku == self.sku

    def __hash__(self):
        return hash(self.sku)
