from pizza_maker import PizzaMaker
from my_pizza import MyPizzaBuilder

pizza_maker = PizzaMaker(MyPizzaBuilder())
pizza_maker.make_pizza()
pizza = pizza_maker.get_pizza()
pizza.display()