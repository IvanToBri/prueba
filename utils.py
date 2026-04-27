def validate_quantity(amount):
    """Verifica que la cantidad proporcionada sea un entero positivo.

    Args:
        amount (int): La cantidad a validar.

    Returns:
        bool: Verdadero si la cantidad es un entero positivo, Falso en caso contrario.
    """
    return isinstance(amount, int) and amount > 0

def format_message(item, stock):
    """Formatea una cadena informativa sobre el inventario actualizado.

    Args:
        item (str): El nombre del producto.
        stock (int): El nuevo stock disponible del producto.

    Returns:
        str: Una cadena formateada indicando el estado del inventario.
    """
    return f"El producto '{item}' ahora tiene {stock} unidades en total."