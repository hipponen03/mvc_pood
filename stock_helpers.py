import exceptions
from product import Product

stockItems = []

# add item to items
def addItem(name, price, amount):
    global stockItems
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in stockItems:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        items.append(product)
# show items
def showItems():
    global stockItems
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("There are no items to show.")
    else:
        return items
# show item
def showItem(name):
    global stockItems
    # control all items step by step
    for item in stockItems:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Couldn't find item {}.".format(name))
# delete ONE item
def deleteItem(name):
    global stockItems
    for item in items:
        # if the name is the same as we search
        if (item.getName() == name):
            stockItems.remove(item)
        else:
            continue
            raise exceptions.ItemExists("Not found {} item.".format(name))
# delete all
def deleteAll():
    global stockItems
    stockItems.clear()

# update item
def updateItem(name, price, amount):
    global stockItems
    for item in stockItems:
        if (item.getName() == name):
            price = item.setPrice(price)
            amount = item.setAmount(amount)
        else:
            raise exceptions.ItemNotExists("Item {} can't be updated, because it does not exist.".format(name))