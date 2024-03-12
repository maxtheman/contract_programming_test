from typing import TYPE_CHECKING, TypeVar, Any
if TYPE_CHECKING:
    from .app import Item

T = TypeVar('T') 

def check_quantity_positive(self: Any, item: 'Item', quantity: int) -> bool:
    """
    Check if the quantity is greater than 0.

    :param item: The item being added.
    :param quantity: The quantity of the item.
    :return: True if the quantity is greater than 0, False otherwise.
    """
    return quantity > 0