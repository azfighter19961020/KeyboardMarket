from django.shortcuts import render
from tools.R import R
from .models import Product
from tools.db import ProductStatus,ProductCategory

# Create your views here.
def product(request,categoryID = None,productID = None):
	if 'category' in request.path:
		return R.ok(ProductCategory.dict())
	if request.method == "GET" and categoryID is not None:
		print(type(categoryID))
		print(type(ProductCategory.list()[0]))
		if not categoryID.isdigit():
			return R.badRequest("categoryID is number only!")
		if int(categoryID) not in ProductCategory.list():
			return R.badRequest("category ID does not exist")
		products = Product.objects.filter(status = ProductStatus.activate.value).filter(category = categoryID)
		products = [i.toJson() for i in products]
		return R.ok(products)
	if request.method == "GET" and productID is not None:
		product = Product.objects.filter(id = productID)
		if not product:
			return R.badRequest("productID does not exist")
		product = product[0]
		return R.ok(product.toJson())
	if request.method == "GET":
		products = Product.objects.filter(status = ProductStatus.activate.value)
		products = [i.toJson() for i in products]
		return R.ok(products)
	return R.methodNotAllowed("method not allowed")