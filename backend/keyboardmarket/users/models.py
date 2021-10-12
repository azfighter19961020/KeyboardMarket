from django.db import models

# Create your models here.

class User(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 255,verbose_name = "用戶名稱")
	password = models.CharField(max_length = 255,verbose_name = "密碼")
	phone = models.CharField(max_length = 255,verbose_name = "電話")
	address = models.CharField(max_length = 255,verbose_name = "地址")
	created_time = models.DateTimeField(auto_now = True)
	modified_time = models.DateTimeField(auto_now = True)
	avatar = models.ImageField(upload_to = "avatar/")
	email = models.CharField(max_length = 255,verbose_name = "電子郵箱")

	def toJson(self):
		data = {}
		data["username"] = self.name
		data["password"] = ""
		data["phone"] = self.phone
		data["address"] = self.address
		data["created_time"] = self.created_time
		data["modified_time"] = self.modified_time
		data["avatar"] = self.avatar.url
		data["email"] = self.email
		return data

	class Meta:
		db_table = "users"