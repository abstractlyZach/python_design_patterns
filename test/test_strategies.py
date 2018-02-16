import pytest
from strategy import fedex_strategy
from strategy import shipping_cost
from strategy import order
from strategy import postal_strategy
from strategy import ups_strategy

strategy_parameters = [
    ('StrategyClass', 'expected_price'),
    [
        (fedex_strategy.FedexStrategy, 3),
        (ups_strategy.UpsStrategy, 4),
        (postal_strategy.PostalStrategy, 5)
    ]
]

@pytest.mark.parametrize(*strategy_parameters)
def test_fedex_strategy(StrategyClass, expected_price):
    test_order = order.Order()
    cost_calculator = shipping_cost.ShippingCost(StrategyClass())
    actual_price = cost_calculator.shipping_cost(test_order)
    assert expected_price == actual_price