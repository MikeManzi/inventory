from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from database import Base

class Inventory(Base):
    __tablename__ = 'inventories'

    inventory_id = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)
    products = relationship("Product", back_populates="inventory", cascade="all, delete-orphan")
    

    def __str__(self):
        return f"Inventory ID: {self.inventory_id}\n Capacity: {self.capacity}\n Current Products: {len(self.products)}/{self.capacity}"