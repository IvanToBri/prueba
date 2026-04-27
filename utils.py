def validate_quantity(amount):
    """Valida que la cantidad sea un número entero positivo.

    Args:
        amount (int): La cantidad a validar.

    Returns:
        bool: True si la cantidad es un entero positivo, False en caso contrario.
    """
    return isinstance(amount, int) and amount > 0

def format_message(item, stock):
    """Formatea una cadena que indica el estado actual del inventario de un producto.

    Args:
        item (str): El nombre del producto.
        stock (int): El número de unidades disponibles del producto.

    Returns:
        str: Una cadena formateada que muestra el estado del inventario.
    """
    return f"El producto '{item}' ahora tiene {stock} unidades en total."