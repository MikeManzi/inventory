from random import randint
from Product import Product
from Inventory import Inventory
from database import Base, engine, Session

Base.metadata.create_all(engine)

class InventoryManager:
    def __init__(self):
        self._session = Session()
        # self.user = user

    @staticmethod
    def _generate_id():
        return randint(1, 1000000)

    def create_inventory(self, capacity):
        inventory_id = self._generate_id()
        inventory = Inventory(inventory_id=inventory_id, capacity=capacity)
        self._session.add(inventory)
        self._session.commit()
        print(f"Inventory {inventory_id} created successfully!")
        return inventory
    
    def add_product(self, inventory_id, product_id, name, price, quantity):
        product = Product(id=product_id, name=name, price=price, quantity=quantity)
        inventory = self._get_inventory_by_id(inventory_id)
        
        if inventory:
            if len(inventory.products) >= inventory.capacity:
                print(f"Inventory {inventory_id} is full!")
                return None
            
            inventory.products.append(product)
            self._session.commit()
            print(f"Product {product_id} added to inventory {inventory_id} successfully!")
            return product
        
        return None
    
    def update_product(self, inventory_id, product_id, name, price, quantity):
        product = self._get_product_by_id(product_id)
        inventory = self._get_inventory_by_id(inventory_id)

        if not product or not inventory:
            return None

        product.name = name if name else product.name
        product.price = price if price else product.price
        product.quantity = quantity if quantity else product.quantity
        self._session.commit()
        print(f"Product {product_id} updated successfully!")
        return inventory
    
    def remove_product(self, inventory_id, product_id):
        product = self._get_product_by_id(product_id)
        inventory = self._get_inventory_by_id(inventory_id)
        if inventory:
            if product in inventory.products:
                inventory.products.remove(product)
                self._session.commit()
                print(f"Product {product_id} removed from inventory {inventory_id} successfully!")
                return product
            else:
                print(f"Product {product_id} not found in inventory {inventory_id}!")
                return None
        return None

    @property
    def inventories(self):
        return self._session.query(Inventory).all()
    
    def get_products_in_inventory(self, inventory_id):
        inventory = self._get_inventory_by_id(inventory_id)
        if inventory:
            return inventory.products
        
        return None
    
    def update_inventory_capacity(self, inventory_id, capacity):
        inventory = self._get_inventory_by_id(inventory_id)
        if inventory:
            inventory.capacity = capacity
            self._session.commit()
            print(f"Inventory {inventory_id} capacity updated successfully!")
            return inventory
        
        return None
    
    def delete_inventory(self, inventory_id):
        inventory = self._get_inventory_by_id(inventory_id)
        if inventory:
            self._session.delete(inventory)
            self._session.commit()
            print(f"Inventory {inventory_id} deleted successfully!")
            return inventory
        
        return None
    
    def _get_inventory_by_id(self, id):
        inventory = self._session.query(Inventory).filter(Inventory.inventory_id == id).first()
        if not inventory:
            print(f"Inventory {id} not found!")
            return None
        return inventory

    def _get_product_by_id(self, id):
        product = self._session.query(Product).filter(Product.id == id).first()
        if not product:
            print(f"Product {id} not found!")
            return None
        return product
