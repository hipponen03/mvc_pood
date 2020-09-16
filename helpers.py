import exceptions


# represents shop structure
# list of Product type objects
items = []

# add item to items

def addItem(name, price, amount):
    global items
    # create the product with require description
    product = Product(name, price, amount)
    if product in items:
        raise exceptions.ItemExists("Item {} exists".format(name))
    else:
        items.append(product)
