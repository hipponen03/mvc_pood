class View:
    # show items
    def showItems(self, items):
        print("Shop items:")
        print("============================")
        print("name\t|\tprice\t|\tamount")
        for item in items:
            print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
            print("============================")
        print("============================")
    # show item
    def showItem(self, item):
        print("Shop item {}".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
        print("============================")

    # no item error
    def noItemError(self, name):
        print("============================")
        print("Shop does not have item {} in it".format(name))
        print("============================")

    # no item to update error
    def noItemToUpdateError(self, name):
        print("============================")
        print("Couldn't update item {}".format(name))
        print("============================")

    # update item
    def updateItem(self, name):
        print("Shop item {} has been updated".format(name))
        print("============================")

    # no item to delete error
    def noItemToDeleteError(self, name):
        print("============================")
        print("Coudln't delete item {}".format(name))
        print("============================")

    # delete item
    def deleteItem(self, name):
        print("Shop item {} has been deleted".format(name))
        print("============================")

    # delete all items
    def deleteItems(self):
        print("All shop items are deleted")
        print("============================")
    # delete all items error
    def noItemsToDeleteError(self):
        print("============================")
        print("Couldn't delete all items")
        print("============================")