import helpers
import stock_helpers

class Model:
    # get shop data - [] of products
    def __init__(self, items):
        self.items = items
    # show items
    def showItems(self):
        return helpers.showItems()
    # show item
    def showItem(self, name):
        return helpers.showItem(name)
    # delete item
    def deleteItem(self, name):
        helpers.deleteItem(name)
    # delete all items
    def deleteAll(self):
        helpers.deleteAll()
    # elemendi uuendamine
    def updateItem(self, name, price, amount):
        helpers.updateItem(name, price, amount)

    def restockItem(self, name, price, amount):
        helpers.addItem(name, price, amount)
        stock_helpers.transferItem(name, amount)