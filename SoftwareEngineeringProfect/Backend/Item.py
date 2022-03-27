import datetime
from Inventory import Inventory as Inv
class Item(object):

	IDCounter = 1
	"""
	constructor called after ensuring all items passed
	are valid
	"""
	def __init__(self , Type , price , quantity , ManufacturerID, VehicalType , StartDate = datetime.date.today()):
		SameTypeItems=Inv.searchMap[Type]
		found=False
		id=0
		for(itemID,item) in SameTypeItems.items():
			if(item.getManufacturerID()==ManufacturerID and item.getVehicalType()==VehicalType):
				found=True
				id=itemID
				break
		if(found):
			self.searchMap[Type][id][ManufacturerID].quantity += 1	
		else: 
			self.userID = Item.IDCounter
			Item.IDCounter += 1
			self.Type = Type
			self.price = price
			self.quantity = quantity
			self.ManufacturerID = ManufacturerID
			self.VehicalType = VehicalType
			self.StartDate = StartDate


	
	def getID(self):
		return self.userID
	
	def getType(self):
		return self.type
	
	def getPrice(self):
		return self.price

	def getQuantity(self):
		return self.quantity

	def getManufacturerID(self):
		return self.ManufacturerID

	def getVehicalType(self):
		return self.VehicalType

	def getStartDate(self):
		return self.StartDate

	#save in database or GUI
	def save():
		pass
	
	#delete from database or GUI
	def delete():
		pass

	#update the quantity of an item after it's some quantity is sold
	def updateSale(self , numSold):
		if(self.quantity >= numSold):
			self.quantity -= numSold
		else:
			print("Not enough quantity to complete your order ")



		