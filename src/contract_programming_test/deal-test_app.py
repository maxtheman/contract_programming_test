# '''
# This file doesn't work.

# Deal isn't set up to work correctly with hypothesis as far as I can see.

# FAILED src/contract_programming_test/test_app.py::test_add_item - TypeError: validate_add_item_quantity() got multiple values for argument 'item'
# Happens no matter what the first argument is. Seems to be an error in _validators.py
# '''

# from contract_programming_test.app import add_item, CashRegister, Item
# import deal
# import hypothesis
# from hypothesis import given
# import pytest
# import hypothesis.strategies as st

# settings = hypothesis.settings(
#     verbosity=hypothesis.Verbosity.verbose,
# )

# register_strategy = st.builds(CashRegister, total=st.floats(allow_nan=False, allow_infinity=False), tax=st.floats(allow_nan=False, allow_infinity=False))
# item_strategy = st.builds(Item)
# quantity_strategy = st.floats(allow_nan=False, allow_infinity=False)

# # @given(register=register_strategy, item=item_strategy, quantity=quantity_strategy)
# # def test_add_item_with_hypothesis(register: CashRegister, item: Item, quantity: float):
# #     # Your test logic here. For example:
# #     initial_total = register.total
# #     register.add_item(item, quantity)
# #     assert register.total >= initial_total  # Adjust this assertion based on your actual logic

# register = CashRegister()

# @deal.cases(
#     register.add_item,
#     kwargs={
#         "quantity": quantity_strategy,
#         'item': item_strategy,
#     },
# )
# def test_add_item(case: deal.TestCase):
#     case()

# # test_set_total = deal.cases(register.set_total)
