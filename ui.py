# import classes and files

from shop import Shop
from product import Product

# create products
bread = Product("bread", 0.80, 10)
milk = Product("milk", 0.50, 50)
wine = Product("wine", 5.60, 5)


# create shop & add products to the shop
shop = Shop()
shop.addProduct(bread)
shop.addProduct(milk)
shop.addProduct(wine)


# test shop content
print(shop)
