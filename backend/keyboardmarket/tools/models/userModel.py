import json

class UserModel:
	def __init__(self,username = "",password = "",password1 = "",phone = "",email = "",address = ""):
		self.username = username
		self.password = password
		self.password1 = password1
		self.phone = phone
		self.email = email
		self.address = address

	def fromJson(self,data):
		jsondata = json.loads(data)
		self.username = jsondata["username"] if "username" in jsondata else None
		self.password = jsondata["password"] if "password" in jsondata else None
		self.password1 = jsondata["password1"] if "password1" in jsondata else None
		self.phone = jsondata["phone"] if "phone" in jsondata else None
		self.email = jsondata["email"] if "email" in jsondata else None
		self.address = jsondata["address"] if "address" in jsondata else None

	def __str__(self):
		return "UserModel[username=%s,password=%s,password1=%s,phone=%s,email=%s,address=%s" % (self.username,self.password,self.password1,self.phone,self.email,self.address)


