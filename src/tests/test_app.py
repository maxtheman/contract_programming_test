from contract_programming_test.app import CashRegister, Item
import hypothesis
from hypothesis import given
import hypothesis.strategies as st
from hypothesis.stateful import RuleBasedStateMachine, rule

settings = hypothesis.settings(
    verbosity=hypothesis.Verbosity.verbose,
)

register_strategy = st.builds(
    CashRegister,
    total=st.floats(allow_nan=False, allow_infinity=False, min_value=0),
    tax=st.floats(allow_nan=False, allow_infinity=False, min_value=0),
)
item_strategy = st.builds(
    Item,
    name=st.text(),
    price=st.floats(allow_nan=False, allow_infinity=False, min_value=0),
    tax=st.floats(allow_nan=False, allow_infinity=False, min_value=0),
)
quantity_strategy = st.integers(min_value=0)


# @given(register=register_strategy, item=item_strategy, quantity=quantity_strategy)
# def test_add_item_with_hypothesis(register: CashRegister, item: Item, quantity: int):
#     initial_total = register.total
#     register.add_item(item, quantity)
#     assert register.total >= initial_total


# @given(
#     register=register_strategy,
#     total=st.floats(allow_nan=False, allow_infinity=False, min_value=0),
# )
# def test_fuzz_CashRegister_set_total(register: CashRegister, total: float) -> None:
#     total = register.set_total(total)
#     assert total == register.total


class CashRegisterStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.register = CashRegister(total=0, tax=0)

    @rule(
        item=item_strategy,
        quantity=quantity_strategy,
    )
    def add_item(self, item: Item, quantity: int):
        initial_total = self.register.total
        self.register.add_item(item, quantity)
        assert self.register.total >= initial_total

    @rule(total=st.floats(allow_nan=False, allow_infinity=False, min_value=0))
    def set_total(self, total: float):
        self.register.set_total(total)  
        assert self.register.total == total

TestCashRegister = CashRegisterStateMachine.TestCase
TestCashRegister.settings = settings