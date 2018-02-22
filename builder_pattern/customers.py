import abs_builder

class WeirdPizzaBuilder(abs_builder.AbsBuilder):
    def make_crust(self):
        self._pizza.crust = 'whole wheat'

    def add_sauce(self):
        self._pizza.sauce = 'tomato'

    def add_meat(self):
        self._pizza.meat = 'sausage'

    def add_veggies(self):
        self._pizza.veggies = 'onions and olives'

    def add_cheese(self):
        self._pizza.topping = 'provolone'
