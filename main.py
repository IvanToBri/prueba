from database import InventoryDB
from utils import validate_quantity, format_message

def restock_item(db, item, amount):
    """
    Restockea una cantidad específica de productos en la base de datos.

    Args:
        db (InventoryDB): La instancia de la base de datos de inventario.
        item (str): El nombre del producto a restockear.
        amount (int): La cantidad de productos a restockear.

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