import datetime
class Inventory():
	searchMap={}
	def __init__(self,itemsList,manufacturerList,currentDate=datetime.date.today()):
		Inventory.searchMap={}
		for item in itemsList:
			Inventory.searchMap[item.getType()][item.getID()][item.getManufacturerID()]=item
		self.itemList = itemsList
		self.manufacturerList = manufacturerList
		self.currentDate = currentDate
	
	def retrieveData(self):
		print("Retrieving data from database...")
		for itemType in Inventory.searchMap:
			for itemID in Inventory.searchMap[itemType]:
				for manufacturerID in Inventory.searchMap[itemType][itemID]:
					print('User ID: '+str(itemID)+'\n'+'Item Type: '+str(itemType)+'\n'+'Price: '+str(Inventory.searchMap[itemType][itemID][manufacturerID].getPrice())+'\n'+'Quantity: '+str(Inventory.searchMap[itemType][itemID][manufacturerID].getQuantity())+'\n'+'Manufacturer ID: '+str(manufacturerID)+'\n'+'Vehical Type: '+str(Inventory.searchMap[itemType][itemID][manufacturerID].getVehicalType())+'\n')
		for item in self.itemsList:
			print('User ID: '+str(item.getID())+'\n'+'Item Type: '+str(item.getType())+'\n'+'Price: '+str(item.getPrice())+'\n'+'Quantity: '+str(item.getQuantity())+'\n'+'Manufacturer ID: '+str(item.getManufacturerID())+'\n'+'Vehical Type: '+str(item.getVehicalType())+'\n')
		for manufacturer in self.manufacturerList:
			print('User ID: '+str(manufacturer.getID())+'\n'+'Name: '+str(manufacturer.getName())+'\n'+'Address: '+str(manufacturer.getAddress())+'\n')
		print("Data retrieved successfully.")
	
	def removeItem(self,itemID):
		pass