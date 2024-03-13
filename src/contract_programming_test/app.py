"""
This module defines the data models used for handling quotes for a fictional bookstore.

It includes:
- `Quote`: Represents a quote, containing multiple line items.
- `LineItem`: Represents a single item within a quote, detailing the item, its quantity, and its genre.
- `LineItemGenre`: An enumeration of possible genres for line items.

These models are utilized throughout the application to manage and process quotes, ensuring data consistency and validation via Pydantic models.
"""
from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from dataclasses import dataclass

class Quote(BaseModel):
    quote_name: str
    line_items: 'List[LineItem]'

class LineItem(BaseModel):
    item: 'Item'
    quantity: int
    genre: 'LineItemGenre'

class LineItemGenre(str, Enum):
    book = "book"
    music = "music"
    movie = "movie"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@dataclass
class CashRegister:
    """A cash register for a store."""
    total: float = 0.0
    tax: float = 0
    # line_items: List[LineItem] = field(default_factory=list)

    def add_item(self, item: Item, quantity: int):
        self.total += item.price * quantity
        if item.tax:
            self.tax += item.tax * quantity
        return self.total

    def set_total(self, total: float):
        self.total = total
        return self.total