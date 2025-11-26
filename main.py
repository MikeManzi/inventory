from InventoryManager import InventoryManager
from User import User

def display_products(products):
    if not products:
        print("\nNo products found in this inventory!")
        return
    
    print("\n" + "="*40)
    print("Products in Inventory")
    print("="*40)
    for product in products:
        print(product)
    print("="*40)


def display_inventories(inventories):
    if not inventories:
        print("\nNo inventories found!")
        return
    
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
    
    print(f"Welcome, {user.email}!")
    inventory_manager = InventoryManager()

    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (1-9): ")

            if choice == '1':
                # Create New Inventory
                capacity = int(input("Enter inventory capacity: "))
                inventory_manager.create_inventory(capacity)

            elif choice == '2':
                # Add Product to Inventory
                inventory_id = int(input("Enter inventory ID: "))
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                inventory_manager.add_product(inventory_id, name, price, quantity)

            elif choice == '3':
                # View All Inventories
                inventories = inventory_manager.inventories
                display_inventories(inventories)

            elif choice == '4':
                # View Products in Inventory
                inventory_id = int(input("Enter inventory ID: "))
                products = inventory_manager.get_products_in_inventory(inventory_id)
                display_products(products)

            elif choice == '5':
                # Update Product
                inventory_id = int(input("Enter inventory ID: "))
                product_id = int(input("Enter product ID: "))
                name = input("Enter new product name (leave blank to keep current): ")
                price_input = input("Enter new product price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                quantity_input = input("Enter new product quantity (leave blank to keep current): ")
                quantity = int(quantity_input) if quantity_input else None
                inventory_manager.update_product(inventory_id, product_id, name, price, quantity)

            elif choice == '6':
                # Update Inventory Capacity
                inventory_id = int(input("Enter inventory ID: "))
                capacity = int(input("Enter new capacity: "))
                inventory_manager.update_inventory_capacity(inventory_id, capacity)

            elif choice == '7':
                # Delete Product
                inventory_id = int(input("Enter inventory ID: "))
                product_id = int(input("Enter product ID: "))
                inventory_manager.remove_product(inventory_id, product_id)

            elif choice == '8':
                # Delete Inventory
                inventory_id = int(input("Enter inventory ID: "))
                confirm = input(f"Are you sure you want to delete inventory {inventory_id}? (yes/no): ")
                if confirm.lower() == 'yes':
                    inventory_manager.delete_inventory(inventory_id)

            elif choice == '9':
                # Exit
                print("\nThank you for using the Inventory Management System!")
                break

            else:
                print("\nInvalid choice! Please enter a number between 1-9.")

        except ValueError as e:
            print(f"\nError: Invalid input! Please enter valid numbers. ({e})")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            print("Thank you for using the Inventory Management System!")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\nFatal error: {e}")
        print("The application has encountered an error and needs to close.")