class Owner(object):
	def __init__(self, name, username, password):
		self.name = name
		self.username =username
		self.password = password

	def getName(self):
		return self.name

	def setName(self):
		while(True):
			self.name=input("Enter your name: ")
			# If name contains symbols,then ask again for name
			if(self.name != '' and all(chr.isalpha() or chr.isspace() for chr in self.name)):
				break
			else:
				print("Invalid name. Please enter again.")
	
	def getUsername(self):
		return self.username
	
	def setUsername(self):
		while(True):
			self.username=input("Enter your username: ")
			# If username contains symbols,then ask again for username
			if(self.username != '' and all(chr.isalnum() for chr in self.username)):
				break
			else:
				print("Invalid username. Please enter again.")

