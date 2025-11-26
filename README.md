# Inventory Management System

A simple inventory management system built with Python and SQLAlchemy.

## Features

- User authentication
- Create and manage multiple inventories
- Add, update, and remove products
- Set inventory capacity limits
- View all inventories and products
- SQLite database persistence

## Requirements

- Python 3.x
- SQLAlchemy

## Installation

```bash
pip install sqlalchemy
```

## Usage

Run the application:

```bash
python main.py
```

Default credentials are stored in `users.csv`.

## Project Structure

- `main.py` - Main application entry point
- `InventoryManager.py` - Core inventory management logic
- `Inventory.py` - Inventory model
- `Product.py` - Product model
- `User.py` - User authentication
- `database.py` - Database configuration
- `inventory.db` - SQLite database file

## Database Schema

**Inventory**
- `inventory_id` (Primary Key)
- `capacity` (Integer)

**Product**
- `id` (Primary Key)
- `name` (String)
- `price` (Float)
- `quantity` (Integer)
- `expiration_date` (Date, optional)
- `inventory_id` (Foreign Key)

