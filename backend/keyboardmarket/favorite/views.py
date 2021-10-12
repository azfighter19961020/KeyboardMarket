from tools.login_check import logincheck
from tools.R import R
from favorite.models import Favorite
from users.models import User
from product.models import Product
from tools.db import FavoriteStatus
import json

# Create your views here.

@logincheck("GET","POST")
def favorite(request,productID = None):
	if request.method == "GET" and productID:
		req = request.GET
		if "username" not in req:
			return R.badRequest("username does not exist")
		username = req["username"]
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("User not found")
		user = user[0]
		product = Product.objects.filter(id = productID)
		if not product:
			return R.badRequest("Product does not exist")
		product = product[0]
		favorite = Favorite.objects.filter(user = user).filter(product = product)
		data = {
			"status":0
		}
		if favorite:
			data["status"] = favorite[0].status
		return R.ok(data)
	if request.method == "GET":
		req = request.GET
		if "username" not in req:
			return R.badRequest("username does not exist")
		username = req["username"]
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("User not found")
		user = user[0]
		favorites = Favorite.objects.filter(user = user).filter(status = FavoriteStatus.activate.value)
		favorites = [i.toJson() for i in favorites]
		return R.ok(favorites)

	if request.method == "POST":
		req = request.body
		data = json.loads(req)
		if "username" not in data or "pid" not in data:
			return R.badRequest("not enough parameters!")
		username = data["username"]
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("User not found")
		user = user[0]
		pid = data["pid"]
		product = Product.objects.filter(id = pid)
		if not product:
			return R.badRequest("product does not exist!")
		product = product[0]
		favorite = Favorite.objects.filter(user = user).filter(product = product)
		if not favorite:
			favorite = Favorite.objects.create(
				user = user,
				product = product,
				status = FavoriteStatus.activate.value
			)
		else:
			favorite = favorite[0]
			if favorite.status == FavoriteStatus.activate.value:
				favorite.status = FavoriteStatus.deactivate.value
			else:
				favorite.status = FavoriteStatus.activate.value
		favorite.save()
		return R.ok({"status":favorite.status})

	return R.methodNotAllowed("method not allowed")
