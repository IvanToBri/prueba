class InventoryDB:
    """Clase que maneja la base de datos de inventario."""

    def __init__(self):
        """Inicializa una instancia de InventoryDB con productos predeterminados."""
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item):
        """
        Obtiene la cantidad disponible de un producto en el inventario.

        Args:
            item (str): El nombre del producto para consultar su stock.

        Returns:
            int: La cantidad disponible del producto, o 0 si no está presente.
        """
        return self._products.get(item.lower(), 0)

    def update_stock(self, item, quantity):
        """
        Actualiza la cantidad disponible de un producto en el inventario.

        Args:
            item (str): El nombre del producto a actualizar.
            quantity (int): Cantidad a agregar al stock.

        Returns:
            bool: True si se actualizó correctamente, False si el producto no estaba en el inventario.
        """
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False