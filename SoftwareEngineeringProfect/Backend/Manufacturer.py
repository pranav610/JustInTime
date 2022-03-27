class Manufacturer(object):
    IDCounter = 1
    """
    constructor called after ensuring all items passed
    are valid
    """
    def __init__(self,name, address):
        self.name = name
        self.address = address
        self.itemCount = 0
        self.userID=Manufacturer.IDCounter
        Manufacturer.IDCounter += 1

    def getUID(self):
        return self.userID

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getItemCount(self):
        return self.itemCount

    def save():
        pass

    def delete():
        pass