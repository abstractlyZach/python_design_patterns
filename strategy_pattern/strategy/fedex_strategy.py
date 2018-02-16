from . import strategy_abc

class FedexStrategy(strategy_abc.Strategy):
    def calculate(self, order):
        return 3