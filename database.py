class InventoryDB:
    """Clase para gestionar la base de datos de inventario.

    Atributos:
        _products (Dict[str, int]): Diccionario que almacena los productos y sus cantidades disponibles.
    """

    def __init__(self):
        """Inicializa una nueva instancia de InventoryDB."""
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item):
        """Obtiene la cantidad disponible de un producto.

        Args:
            item (str): El nombre del producto.

        Returns:
            int: La cantidad disponible del producto.
        """
        return self._products.get(item.lower(), 0)

    def update_stock(self, item, quantity):
        """Actualiza la cantidad disponible de un producto.

        Args:
            item (str): El nombre del producto.
            quantity (int): Cantidad a actualizar.

        Returns:
            bool: True si se actualizó correctamente, False si el producto no existe.
        """
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False