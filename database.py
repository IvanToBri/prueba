class InventoryDB:
    """
    Representa una base de datos de inventario que almacena productos y sus cantidades.

    Args:
        None

    Attributes:
        _products (dict): Un diccionario donde se almacenan los productos y sus cantidades actuales.

    Methods:
        get_stock(item): Devuelve la cantidad actual de un producto dado su nombre.
                        La búsqueda es case-insensitive.
        
        update_stock(item, quantity): Actualiza la cantidad de un producto dado su nombre y la cantidad a sumar.
                                   Si el producto existe, devuelve True; sino, devuelve False.
    """

    def __init__(self):
        """
        Constructor de la clase InventoryDB.

        Args:
            None

        Returns:
            None
        """
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item):
        """
        Obtiene la cantidad actual de un producto dado su nombre.

        Args:
            item (str): El nombre del producto.

        Returns:
            int: La cantidad actual del producto.
        """
        return self._products.get(item.lower(), 0)

    def update_stock(self, item, quantity):
        """
        Actualiza la cantidad de un producto dado su nombre y la cantidad a sumar.

        Args:
            item (str): El nombre del producto.
            quantity (int): La cantidad a sumar al producto.

        Returns:
            bool: True si el producto existe y se ha actualizado correctamente, False en caso contrario.
        """
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False