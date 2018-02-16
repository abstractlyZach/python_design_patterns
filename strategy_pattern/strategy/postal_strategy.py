from . import strategy_abc

class PostalStrategy(strategy_abc.Strategy):
    def calculate(self, order):
        return 5