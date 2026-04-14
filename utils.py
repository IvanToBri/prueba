def validate_quantity(amount):
    """Valida que la cantidad sea un número entero y positivo."""
    
    # Verifica si 'amount' es un entero y mayor a cero
    if not isinstance(amount, int) or amount <= 0:
    
    return True

def format_message(item, stock):
    """Formatea una cadena informativa sobre el inventario actualizado."""
    
    # Devuelve una cadena formateada indicando las unidades disponibles del artículo
    return f"El producto '{item}' ahora tiene {stock} unidades en total."

# Ejemplo de uso:
try:
    print(validate_quantity(5))  # Debería devolver True
    print(format_message('Camiseta', 12))  # Debería imprimir "El producto 'Camiseta' ahora tiene 12 unidades en total."
except ValueError as e:
    print(e)