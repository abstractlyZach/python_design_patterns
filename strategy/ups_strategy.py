from . import strategy_abc

class UpsStrategy(strategy_abc.Strategy):
    def calculate(self, order):
        return 4