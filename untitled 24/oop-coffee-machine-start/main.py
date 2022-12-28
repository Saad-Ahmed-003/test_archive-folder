from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
latte = MenuItem(name="latte", water=100, milk=250, coffee=24, cost=2.5)
a = menu.get_items()
print(menu.get_items())
