def validate_quantity(amount):
    """Valida que la cantidad sea un número entero positivo.

    Args:
        amount (int): La cantidad a validar.

    Returns:
        bool: Verdadero si la cantidad es un número entero positivo, Falso en caso contrario.
    """
    return isinstance(amount, int) and amount > 0

def format_message(item, stock):
    """Formatea una cadena de texto con el nombre del producto y su nuevo inventario.

    Args:
        item (str): El nombre del producto.
        stock (int): El nuevo inventario del producto.

    Returns:
        str: Una cadena formateada indicando el nombre del producto y su nuevo inventario.
    """
    return f"El producto '{item}' ahora tiene {stock} unidades en total."