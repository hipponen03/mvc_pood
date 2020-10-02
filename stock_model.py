

class StockModel:
    # get shop data - [] of products
    def __init__(self, stockItems):
        self.stockItems = stockItems
    # add item to stockItems
    def addItem(self, name, price, amount):
        stock_helpers.addItem(name, price, amount)
    # show items
    def showItems(self):
        return stock_helpers.showItems()
    # show item
    def showItem(self, name):
        return stock_helpers.showItem(name)
    # delete item
    def deleteItem(self, name):
        stock_helpers.deleteItem(name)
    # delete all items
    def deleteAll(self):
        stock_helpers.deleteAll()
    # elemendi uuendamine
    def updateItem(self, name, price, amount):
        stock_helpers.updateItem(name, price, amount)