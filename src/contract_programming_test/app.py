"""
This module defines the data models used for handling quotes for a fictional bookstore.

It includes:
- `Quote`: Represents a quote, containing multiple line items.
- `LineItem`: Represents a single item within a quote, detailing the item, its quantity, and its genre.
- `LineItemGenre`: An enumeration of possible genres for line items.

These models are utilized throughout the application to manage and process quotes, ensuring data consistency and validation via Pydantic models.
"""
from contract_programming_test.contracts import check_quantity_positive
from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from dataclasses import dataclass
# import deal
import icontract

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

# @icontract.invariant(lambda self: self.tax >= 0)
# @icontract.invariant(lambda self: self.total >= self.tax)
@dataclass
@icontract.invariant(lambda self: self.total >= 0)
class CashRegister:
    total: float = 0
    tax: float = 0

    @icontract.require(check_quantity_positive)
    def add_item(self, item: Item, quantity: int):
        self.total += item.price * quantity
        if item.tax:
            self.tax += item.tax * quantity

    def set_total(self, total: float):
        self.total = total

if __name__ == "__main__":
    register = CashRegister()
    item = Item(name="Book", price=10)
    register.add_item(item, 1)
    register.set_total(-10)
    print(register.total)

