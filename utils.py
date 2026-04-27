def validate_quantity(amount):
    """Verifica si la cantidad proporcionada es un número entero positivo.

    Args:
        amount (int): La cantidad a verificar.

    Returns:
        bool: True si la cantidad es un número entero positivo, False en caso contrario.

    Raises:
        TypeError: Si la entrada no es un número entero.
    """
    if not isinstance(amount, int):
        raise TypeError("La cantidad debe ser un número entero.")
    return amount > 0

def format_message(item, stock):
    """Formatea una cadena que indica la actualización del inventario.

    Args:
        item (str): El nombre del producto.
        stock (int): La nueva cantidad disponible del producto.

    Returns:
        str: Una cadena formateada indicando la actualización del inventario.
    """
    return f"El producto '{item}' ahora tiene {stock} unidades en total."