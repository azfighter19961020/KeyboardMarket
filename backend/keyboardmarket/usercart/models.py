from django.db import models
from product.models import Product
from users.models import User

# Create your models here.

class Cart(models.Model):
	id = models.AutoField(primary_key = True)
	product = models.ForeignKey(Product,on_delete = models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	amount = models.IntegerField(verbose_name = "商品數量")
	status = models.IntegerField(verbose_name = "狀態")
	created_time = models.DateTimeField(auto_now = True)
	modified_time = models.DateTimeField(auto_now = True)

	def toJson(self):
		data = {}
		data["id"] = self.id
		data["product"] = self.product.toJson()
		data["username"] = self.user.name
		data["amount"] = self.amount
		data["status"] = self.status
		data["created_time"] = self.created_time
		data["modified_time"] = self.modified_time
		return data

	class Meta:
		db_table = "usercart"