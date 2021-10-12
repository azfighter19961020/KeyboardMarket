from django.db import models
from users.models import User
from product.models import Product

# Create your models here.

class Favorite(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE,verbose_name = "用戶")
	product = models.ForeignKey(Product,on_delete = models.CASCADE,verbose_name = "商品")
	created_time = models.DateTimeField(auto_now = True,verbose_name = "創建時間")
	modified_time = models.DateTimeField(auto_now = True,verbose_name = "修改時間")
	status = models.IntegerField(verbose_name = "狀態")

	def toJson(self):
		data = {}
		data["id"] = self.id
		data["username"] = self.user.name
		data["product"] = self.product.toJson()
		data["created_time"] = self.created_time
		data["modified_time"] = self.modified_time
		data["status"] = self.status
		return data

	class Meta:
		db_table = "favorite"
