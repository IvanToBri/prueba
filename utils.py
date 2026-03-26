def validate_quantity(amount):
    """Asegura que la cantidad sea un número positivo."""
    return isinstance(amount, int) and amount > 0

def format_message(item, stock):
    return f"El producto '{item}' ahora tiene {stock} unidades en total."