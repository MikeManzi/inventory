from InventoryManager import InventoryManager
from User import User

def display_products(products):
    print("\n" + "="*40)
    print("Products in Inventory")
    print("="*40)
    for product in products:
        print(product)
    print("="*40)


def display_inventories(inventories):
    print("\n" + "="*40)
    print("Inventories")
    print("="*40)
    for inventory in inventories:
        print(inventory)
    print("="*40)


def display_menu():
    print("\n" + "="*40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Create New Inventory")
    print("2. Add Product to Inventory")
    print("3. View All Inventories")
    print("4. View Products in Inventory")
    print("5. Update Product")
    print("6. Update Inventory Capacity")
    print("7. Delete Product")
    print("8. Delete Inventory")
    print("9. Exit")
    print("="*40)


def main():
    print("="*40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*40)

    # Login
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = User.login(email, password)

    if not user:
        print("Invalid email or password!")
        return

    inventory_manager = InventoryManager()
    inventory = inventory_manager.create_inventory(100)
    inventory_manager.create_inventory(200)

    # Add products to inventory
    inventory_manager.add_product(inventory.inventory_id, 1, "Empress Eugénie tiara", 100, 10)
    inventory_manager.add_product(inventory.inventory_id, 2, "Reliquary brooch", 200, 20)
    inventory_manager.add_product(inventory.inventory_id, 3, "Sapphire tiara", 300, 30)

    # View products in inventory
    products = inventory_manager.get_products_in_inventory(inventory.inventory_id)
    display_products(products)

    # Update product
    inventory_manager.update_product(inventory.inventory_id, 1, "Empress Eugénie tiara", 200, 10)
    products = inventory_manager.get_products_in_inventory(inventory.inventory_id)
    display_products(products)

    # Remove product
    inventory_manager.remove_product(inventory.inventory_id, 1)
    products = inventory_manager.get_products_in_inventory(inventory.inventory_id)
    display_products(products)

    # Update inventory capacity
    inventory_manager.update_inventory_capacity(inventory.inventory_id, 200)
    inventory = inventory_manager.get_inventory_by_id(inventory.inventory_id)
    print(f"Inventory {inventory.inventory_id} capacity updated to {inventory.capacity}")

    # Delete inventory
    inventory_manager.delete_inventory(inventory.inventory_id)
    inventories = inventory_manager.get_all_inventories()
    display_inventories(inventories)

if __name__ == '__main__':
    main()