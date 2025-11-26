from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(Date, nullable=True)
    inventory_id = Column(Integer, ForeignKey('inventories.inventory_id'))

    inventory = relationship("Inventory", back_populates="products")


    def __str__(self):
        return f"Product ID: {self.id}\n Name: {self.name}\n Price: ${self.price:.2f}\n Quantity: {self.quantity}"
