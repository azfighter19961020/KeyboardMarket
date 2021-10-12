from django.db import models

# Create your models here.

class Product(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 255,verbose_name = "商品名稱")
	price = models.IntegerField(verbose_name = "價格")
	stored_amount = models.IntegerField(verbose_name = "存量")
	created_time = models.DateTimeField(auto_now = True)
	modified_time = models.DateTimeField(auto_now = True)
	status = models.IntegerField(verbose_name = "狀態")
	img = models.ImageField(upload_to = "productImage/")
	category = models.IntegerField(verbose_name = "種類")
	info = models.TextField(verbose_name = "詳細描述")

	def toJson(self):
		data = {}
		data["id"] = self.id
		data["name"] = self.name
		data["price"] = self.price
		data["stored_amount"] = self.stored_amount
		data["created_time"] = self.created_time
		data["modified_time"] = self.modified_time
		data["status"] = self.status
		data["img"] = self.img.url
		data["category"] = self.category
		data["info"] = self.info
		return data

	class Meta:
		db_table = "products"