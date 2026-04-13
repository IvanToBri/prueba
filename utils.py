from typing import Any

def validate_quantity(amount: Any) -> bool:
    """Asegura que la cantidad sea un número positivo.

    Args:
        amount (Any): La cantidad a validar. Puede ser cualquier tipo de dato numérico.

    Returns:
        bool: True si la cantidad es un entero positivo, False en caso contrario.
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("La cantidad debe ser un número.")
    return amount > 0

def format_message(item: str, stock: int) -> str:
    """Formata una cadena de mensaje indicando el stock actualizado de un producto.

    Args:
        item (str): El nombre del producto.
        stock (int): El nuevo stock disponible del producto.

    Returns:
        str: Una cadena de mensaje informativa.
    """
    return f"El producto '{item}' ahora tiene {stock} unidades en total."