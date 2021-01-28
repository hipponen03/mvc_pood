from product import Product
from shop import Shop
from controller_shop import Controller
from model import Model
from view import View
from stock_model import StockModel
from stock import Stock
from controller_stock import ControllerStock
from view_stock import ViewStock

# create shop
shop = Controller(Model(Shop()), View())
# create stock
stock = ControllerStock(StockModel(Stock()), ViewStock())

stock.addItem("wine", 5.60, 5)
stock.showItems()
shop.restockItem("wine", 5.60, 3)
shop.showItems()

stock.showItems()






