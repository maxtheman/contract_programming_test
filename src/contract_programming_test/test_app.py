from contract_programming_test.app import CashRegister
import deal

register = CashRegister()


test_add = deal.cases(register.add_item)
test_set_total = deal.cases(register.set_total)
