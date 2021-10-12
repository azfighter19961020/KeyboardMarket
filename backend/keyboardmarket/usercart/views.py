from tools.R import R
from tools.login_check import logincheck
from .models import Cart
from tools.models.cartModel import CartModel
from product.models import Product
from users.models import User
from tools.db import CartStatus

@logincheck('GET','POST','PUT','DELETE')
def usercart(request,username = None,cid = None):
	print("request.method is:")
	print(request.method)
	if request.method == "GET":
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("User does not exist")
		user = user[0]
		carts = Cart.objects.filter(user = user).filter(status = CartStatus.activate.value)
		carts = [i.toJson() for i in carts]
		return R.ok(carts)
	if request.method == "POST":
		req = request.body
		ucart = CartModel()
		ucart.fromJson(req)
		if ucart.amount == 0:
			return R.badRequest("Add cart amount can not be 0")
		product = Product.objects.filter(id = ucart.product_id)
		if not product:
			return R.badRequest("Product does not exist")
		product = product[0]
		if ucart.amount > product.stored_amount:
			return R.badRequest("Add cart amount reach maximum stored amount")
		user = User.objects.filter(name = ucart.username)
		if not user:
			return R.badRequest("User does not exist")
		user = user[0]
		dbcart = Cart.objects.filter(user = user).filter(product = product).filter(status = CartStatus.activate.value)
		if dbcart:
			dbcart[0].amount += ucart.amount
			dbcart[0].save()
		else:
			cart = Cart.objects.create(
				product = product,
				user = user,
				amount = ucart.amount,
				status = CartStatus.activate.value
			)
			cart.save()
		return R.ok("add cart success")
	elif request.method == "PUT":
		req = request.body
		ucart = CartModel()
		ucart.fromJson(req)
		if ucart.amount == 0:
			return R.badRequest("Cart amount can not be 0")
		product = Product.objects.filter(id = ucart.product_id)
		if not product:
			return R.badRequest("Product does not exist!")
		product = product[0]
		if ucart.amount > product.stored_amount:
			return R.badRequest("Add cart amount reach maximum stored amount")
		user = User.objects.filter(name = ucart.username)
		if not user:
			return R.badRequest("User does not exist!")
		user = user[0]
		dbcart = Cart.objects.filter(user = user).filter(product = product)
		dbcart = dbcart[0]
		dbcart.amount = ucart.amount
		dbcart.save()
		return R.ok("amount change success")
	elif request.method == "DELETE" and cid is not None:
		cid = int(cid)
		cart = Cart.objects.filter(id = cid)
		if not cart:
			return R.badRequest("Cart record does not exist")
		cart = cart[0]
		cart.delete()
		return R.ok("delete success")
	else:
		return R.methodNotAllowed("method not allowed")