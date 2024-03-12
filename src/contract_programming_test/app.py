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
from dataclasses import dataclass, field
import deal
# import icontract

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

@deal.has('io', 'stdout')
@deal.safe
def no_print():
    print('psyche')


@dataclass
@deal.inv(lambda self: self.total >= 0)
class CashRegister:
    total: float = 0
    tax: float = 0
    line_items: List[LineItem] = field(default_factory=list)

    @deal.pure
    @deal.pre(lambda self, item, quantity: quantity > 0)
    def add_item(self, item: Item, quantity: int):
        self.total += item.price * quantity
        if item.tax:
            self.tax += item.tax * quantity

    @deal.pure
    @deal.pre(lambda self, total: total == 0)
    def set_total(self, total: float):
        self.total = total



if __name__ == "__main__":
    # no!
    # no_print()
    register = CashRegister()
    #ok!
    register.add_item(Item(name="book", price=10), 1)
    print(register.total)
    #not ok!
    register.set_total(-1000)

