from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Модель данных, которую будем возвращать
class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

# Пример данных с новыми полями
fake_items = [
    Item(name="Item 1", description="Description of item 1", price=19.99, in_stock=True),
    Item(name="Item 2", description="Description of item 2", price=29.99, in_stock=False),
    Item(name="Item 3", description="Description of item 3", price=39.99, in_stock=True)
]

@app.get("/items", response_model=List[Item], summary="Get list of items", description="Returns a list of items with their details, such as name, description, price, and stock availability.")
async def get_items():
    """
    Этот запрос возвращает список товаров.
    Каждый товар включает:
    - `name`: Название товара
    - `description`: Описание товара
    - `price`: Цена товара
    - `in_stock`: Наличие товара на складе (True/False)
    """
    return fake_items

@app.get("/items/{item_id}", response_model=Item, summary="Get item by ID", description="Returns a single item by its ID with details like name, description, price, and stock availability.")
async def get_item(item_id: int):
    """
    Этот запрос возвращает данные конкретного товара по его ID.
    """
    if item_id < len(fake_items):
        return fake_items[item_id]
    return {"error": "Item not found"}
