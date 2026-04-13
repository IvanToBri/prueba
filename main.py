from database import InventoryDB
from utils import validate_quantity, format_message

def restock_item(db, item, amount):
    """Actualiza la cantidad disponible de un producto en el inventario.

    Args:
        db (InventoryDB): Instancia de la base de datos de inventario.
        item (str): Nombre del producto a restockear.
        amount (int): Cantidad a agregar al stock.

    Returns:
        None
    """
    
    if validate_quantity(amount):
        if db.update_stock(item, amount):
            new_stock = db.get_stock(item)
            print(format_message(item, new_stock))
        else:
            print(f"Error: El producto {item} no existe.")
    else:
        print("Error: Cantidad inválida.")

if __name__ == "__main__":
    mi_db = InventoryDB()
    restock_item(mi_db, "manzana", 5)