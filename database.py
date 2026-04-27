class InventoryDB:
    """Clase que maneja la base de datos de inventario.

    Attributes:
        _products (dict): Diccionario donde se almacenan los productos y sus cantidades disponibles.
    """

    def __init__(self):
        """Inicializa una instancia de InventoryDB."""
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item):
        """Obtiene la cantidad disponible de un producto.

        Args:
            item (str): El nombre del producto a consultar.

        Returns:
            int: La cantidad disponible del producto, o 0 si no está registrado.
        """
        return self._products.get(item.lower(), 0)

    def update_stock(self, item, quantity):
        """Actualiza la cantidad disponible de un producto.

        Args:
            item (str): El nombre del producto a actualizar.
            quantity (int): Cantidad a agregar o restar al producto.

        Returns:
            bool: True si la actualización fue exitosa, False si el producto no estaba registrado.
        """
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False