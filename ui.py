# import classes and files

from shop import Shop
from product import Product
from controller import Controller
from model import Model
from view import View

# create products
bread = Product("bread", 0.80, 10)
milk = Product("milk", 0.50, 50)
wine = Product("wine", 5.60, 5)


# create shop & add products to the shop
shop = Controller(Model(Shop()), View())
shop.addItem("bread", 0.80, 10)
shop.addItem("milk", 0.50, 50)
shop.addItem("wine", 5.60, 5)


