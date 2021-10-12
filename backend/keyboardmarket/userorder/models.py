from django.db import models
from product.models import Product
from users.models import User

# Create your models here.

class Order(models.Model):
	id = models.AutoField(primary_key = True)
	orderno = models.CharField(max_length = 255,verbose_name = "訂單編號")
	product = models.ForeignKey(Product,on_delete = models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	amount = models.IntegerField(verbose_name = "商品數量")
	status = models.IntegerField(verbose_name = "狀態")
	paypal_id = models.CharField(max_length = 255,verbose_name = "paypal訂單編號")
	created_time = models.DateTimeField(auto_now = True)
	modified_time = models.DateTimeField(auto_now = True)


	class Meta:
		db_table = "orders"
