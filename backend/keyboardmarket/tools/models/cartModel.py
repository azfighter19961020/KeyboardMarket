import json

class CartModel:
	def __init__(self,cart_id = 0,product_id = 0,username = "",amount = 0):
		self.cart_id = cart_id
		self.product_id = product_id
		self.username = username
		self.amount = amount

	def fromJson(self,data):
		jsondata = json.loads(data)
		self.cart_id = jsondata["cid"] if "cid" in jsondata else ""
		self.product_id = jsondata["pid"] if "pid" in jsondata else ""
		self.username = jsondata["username"] if "username" in jsondata else ""
		self.amount = jsondata["amount"] if "amount" in jsondata else ""

