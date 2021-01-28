import exceptions

class ControllerStock:
    def __init__(self, model, view):
        self.stock_model = model
        self.view_stock = view

    def addItem(self, name, price, amount):
            self.stock_model.addItem(name, price, amount)

    def showItems(self):
        try:
            items = self.stock_model.showItems()
            self.view_stock.showItems(items)
        except:
            print("No items to show.")

    def showItem(self, name):
        try:
            item = self.stock_model.showItem(name)
            self.view_stock.showItem(item)
        except:
            self.view_stock.noItemError(name)

    def deleteItem(self, name):
        try:
            self.stock_model.deleteItem(name)
            self.view_stock.deleteItem(name)
        except:
            print("Failed to delete item.")

    def deleteAll(self):
        try:
            self.stock_model.deleteAll()
            self.view_stock.deleteAll()
        except:
            print("There are no items to show.")

# elemendi uuendamine
    def updateItem(self, name, price, amount):
        if (price <= 0):
            print("Price must be higher than 0 EUR")
        elif (amount <= 0):
            print("Amount must be higher than 0")
        try:
            self.stock_model.updateItem(name, price, amount)
            self.view_stock.updateItem()
        except:
            self.view_stock.noItemError(name)