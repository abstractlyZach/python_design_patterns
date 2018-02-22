import customers
from pizza_maker import PizzaMaker
from my_pizza import MyPizzaBuilder

my_pizza_maker = PizzaMaker(MyPizzaBuilder())
my_pizza_maker.make_pizza()
pizza = my_pizza_maker.get_pizza()
pizza.display()
print()

customer_pizza_maker = PizzaMaker(customers.WeirdPizzaBuilder())
customer_pizza_maker.make_pizza()
pizza = customer_pizza_maker.get_pizza()
pizza.display()