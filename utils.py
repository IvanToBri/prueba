def validate_quantity(amount):
    """Verifica si una cantidad es un número entero positivo.

    Args:
        amount (int): La cantidad a verificar.

    Returns:
        bool: True si la cantidad es un número entero positivo, False en caso contrario.
    """
    return isinstance(amount, int) and amount > 0

def format_message(item, stock):
    """Formatea un mensaje indicando la cantidad actual del producto.

    Args:
        item (str): El nombre del producto.
        stock (int): La cantidad disponible del producto.

    Returns:
        str: Un mensaje formateado mostrando la cantidad actual del producto.
    """
    return f"El producto '{item}' ahora tiene {stock} unidades en total."