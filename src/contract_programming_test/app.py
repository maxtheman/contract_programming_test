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

def validate_add_item_quantity(item: 'Item', quantity:int):
    return True

def greater_than_zero(num: int) -> bool:
    if num is None:
        num = 0
    return num > 0

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


@deal.pure
@deal.pre(validate_add_item_quantity) #type: ignore
@deal.post(greater_than_zero) #type: ignore
def add_item(register: 'CashRegister', item: Item, quantity: int):
    register.set_total(item.price * quantity)
    if item.tax:
        register.tax += item.tax * quantity
    return register.total

# @deal.inv(lambda self: self.total >= 0) #type: ignore
@dataclass
class CashRegister:
    """A cash register for a store."""
    total: float = 0.0
    tax: float = 0
    # line_items: List[LineItem] = field(default_factory=list)

    @deal.pre(validate_add_item_quantity) #type: ignore
    def add_item(self, item: Item, quantity: int):
        self.total += item.price * quantity
        if item.tax:
            self.tax += item.tax * quantity
        return self.total

    @deal.pure
    @deal.pre(lambda total: total == 0) #type: ignore
    def set_total(self, total: float):
        self.total = total
        return self.total

@deal.raises(ValueError)
@deal.post(lambda r: r >= 0.0)
def plain_addition(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError('a and b must be non-zero')
    return abs(a + b)

if __name__ == "__main__":
    # no!
    # no_print()
    register = CashRegister()
    #ok!
    register.add_item(Item(name="book", price=10), 1)
    print(register.total)
    #not ok!
    register.set_total(-1000)

