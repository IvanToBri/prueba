class InventoryDB:
    """
    Clase que representa una base de datos de inventario.

    Atributos:
        _products (dict): Un diccionario donde se almacenan los productos y sus cantidades disponibles.

    Métodos:
        get_stock(item: str) -> int:
            Devuelve la cantidad disponible del producto especificado.

        update_stock(item: str, quantity: int) -> bool:
            Actualiza la cantidad disponible del producto especificado por la cantidad proporcionada.
            Retorna True si la actualización fue exitosa, False si el producto no existe.
    """

    def __init__(self):
        """
        Constructor de la clase InventoryDB.

        Inicializa el inventario con algunos productos predefinidos.
        """
        self._products = {"manzana": 10, "pan": 5}

    def get_stock(self, item: str) -> int:
        """
        Obtiene la cantidad disponible del producto especificado.

        Args:
            item (str): El nombre del producto.

        Returns:
            int: La cantidad disponible del producto.
        """
        return self._products.get(item.lower(), 0)

    def update_stock(self, item: str, quantity: int) -> bool:
        """
        Actualiza la cantidad disponible del producto especificado por la cantidad proporcionada.

        Args:
            item (str): El nombre del producto.
            quantity (int): La cantidad a agregar al inventario.

        Returns:
            bool: True si la actualización fue exitosa, False si el producto no existe.
        """
        if item.lower() in self._products:
            self._products[item.lower()] += quantity
            return True
        return False