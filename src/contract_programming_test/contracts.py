from typing import TYPE_CHECKING, TypeVar, Any, Optional
if TYPE_CHECKING:
    from .app import Item

T = TypeVar('T') 

def check_quantity_positive(self: Optional[Any] = None, item: Optional['Item'] = None, quantity: Optional[int] = None) -> bool:
    """
    Check if the quantity is greater than 0.

    :param item: The item being added.
    :param quantity: The quantity of the item.
    :return: True if the quantity is greater than 0, False otherwise.
    """
    if item is None or quantity is None:
        return False
    return quantity > 0

