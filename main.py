from database import InventoryDB
from utils import validate_quantity, format_message

def restock_item(db, item, amount):
    """Restoca una determinada cantidad de un artículo en el inventario.

    Args:
        db (InventoryDB): Instancia de la clase InventoryDB para interactuar con el inventario.
        item (str): Nombre del artículo a restockear.
        amount (int): Cantidad a restockear. Debe ser un número positivo.

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