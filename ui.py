from product import Product
from shop import Shop
from controller import Controller
from model import Model
from stock_helpers import stockItems
from view import View
from stock_model import StockModel
from stock import Stock

# create products
bread = Product("bread", 0.80, 10)
milk = Product("milk", 0.50, 50)
wine = Product("wine", 5.60, 5)

# create shop and add products to shop
shop = Controller(Model(Shop()), View())
stock = Controller(StockModel(Stock()), View())

stock.addItem("wine", 5.60, 5)
stock.addItem("bread", 2.30, 10)
stock.showItems()
shop.showItems()
stock.updateItem("wine", 6.00, 10)
# update item ei tööta
# updateitem läheb controllerisse ksu üritatakse uuendata shopi mitte stocki


#shop.showItems()





