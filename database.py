class InventoryDB:
    """Clase que representa una base de datos de inventario.

    Atributos:
        _products (dict): Un diccionario donde las claves son nombres de productos y los valores son cantidades disponibles.

    Métodos:
        get_stock(item):
            Devuelve la cantidad disponible del producto especificado. El nombre del producto se convierte a minúsculas para asegurar que sea case-insensitive.

        update_stock(item, quantity):
            Actualiza la cantidad disponible del producto especificado. Si el producto existe, incrementa su cantidad; de lo contrario, devuelve False.
    """

    def __init__(self):
        """Inicializa la instancia de InventoryDB."""
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item):
        """Devuelve la cantidad disponible del producto especificado.

        Args:
            item (str): Nombre del producto.

        Returns:
            int: Cantidad disponible del producto.
        """
        return self._products.get(item.lower(), 0)

    def update_stock(self, item, quantity):
        """Actualiza la cantidad disponible del producto especificado.

        Args:
            item (str): Nombre del producto.
            quantity (int): Cantidad a agregar al stock.

        Returns:
            bool: True si el producto existe y se actualizó correctamente, False en caso contrario.
        """
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False