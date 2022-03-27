from Owner import Owner

class Login(Owner):
	def __init__(self, name, username, password):
		super().__init__(name, username, password)
		
	def AuthenticateLogin(self):
		# Check if username and password are correct
		UserName=input("Enter your username: ")
		Password=input("Enter your password: ")
		if(self.username == UserName and self.password == Password):
			print("Login successful.")
			return True
		else:
			print("Login failed.")
			return False