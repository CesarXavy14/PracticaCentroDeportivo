class Item:

    items = []

    def __init__(self):
        self.idi = 0
        self.name = ""
        self.quantity = 0
    
    def __repr__(self):
        return str(self.__dict__)

    def addItem(self, newItem):
        self.items.append(newItem)
    
    def getItems(self):
        return self.items

    def getItem(self, idi, name):
        if idi != None:
            for item in self.items:
                if(item.idi == idi):
                    return item
        elif name != None:
            for item in self.items:
                if(item.name == name):
                    return item

    def updateItemSubtraction(self, idi, name, quantity):
        if idi != None:
            for item in self.items:
                if(item.idi == idi and item.quantity >= quantity):
                    item.quantity = item.quantity - quantity
                    return item
        elif name != None:
            for item in self.items:
                if(item.name == name and item.quantity >= quantity):
                    item.quantity = item.quantity - quantity
                    return item
                    
    def updateItemSum(self, idi, name, quantity):
        if idi != None:
            for item in self.items:
                if(item.idi == idi):
                    item.quantity = item.quantity + quantity
                    return item
        elif name != None:
            for item in self.items:
                if(item.name == name and item.quantity >= quantity):
                    item.quantity = item.quantity + quantity
                    return item

    def getId(self, idi, name):
        if idi != None:
            for item in self.items:
                if(item.idi == idi):
                    return item.idi
        elif name != None:
            for item in self.items:
                if(item.name == name):
                    return item.idi

    def getName(self, idi, name):
        if idi != None:
            for item in self.items:
                if(item.idi == idi):
                    return item.name
        elif name != None:
            for item in self.items:
                if(item.name == name):
                    return item.name

    def getQuantity(self, idi, name):
        if idi != None:
            for item in self.items:
                if(item.idi == idi):
                    return item.quantity
        elif name != None:
            for item in self.items:
                if(item.name == name):
                    return item.quantity
