class InventoryDB:
    def __init__(self):
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item):
        return self._products.get(item.lower(), 0)

    def update_stock(self, item, quantity):
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False