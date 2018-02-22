from abs_builder import AbsBuilder

class MyPizzaBuilder(AbsBuilder):
    """My favorite pizza"""

    def make_crust(self):
        self._pizza.crust = 'Whole wheat'

    def add_sauce(self):
        self._pizza.sauce = 'Tomato'

    def add_meat(self):
        self._pizza.meat = 'Sausage and Pepperoni'

    def add_veggies(self):
        self._pizza.veggies = 'Tomatoes and olives'

    def add_cheese(self):
        self._pizza.topping = 'Mozzarella'