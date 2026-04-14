from typing import Dict

class InventoryDB:
    """Clase que representa una base de datos de inventario utilizando ChromaDB.

    Atributos:
        _products (Dict[str, int]): Un diccionario que almacena los productos y sus cantidades disponibles.

    Métodos:
        __init__(): Inicializa la instancia de InventoryDB con un stock predeterminado.

        get_stock(item: str) -> int: Devuelve la cantidad disponible del producto especificado. La búsqueda es case-insensitive.

        update_stock(item: str, quantity: int) -> bool: Actualiza la cantidad del producto especificado. Retorna True si se pudo actualizar correctamente, False en caso contrario.
    """

    def __init__(self):
        """Inicializa la instancia de InventoryDB con un stock predeterminado."""
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item):
        """Devuelve la cantidad disponible del producto especificado. La búsqueda es case-insensitive.

        Args:
            item (str): El nombre del producto cuya cantidad deseamos obtener.

        Returns:
            int: La cantidad disponible del producto.
        """
        return self._products.get(item.lower(), 0)

    def update_stock(self, item, quantity):
        """Actualiza la cantidad del producto especificado. Retorna True si se pudo actualizar correctamente, False en caso contrario.

        Args:
            item (str): El nombre del producto cuyo stock desea actualizar.
            quantity (int): Cantidad a agregar o restar al producto.

        Returns:
            bool: True si se pudo actualizar correctamente, False en caso contrario.
        """
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False