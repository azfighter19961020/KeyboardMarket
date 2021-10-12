from django.shortcuts import render
from tools.R import R
from tools.models.userModel import UserModel
from users.models import User
import hashlib
from tools.token import make_token

# Create your views here.

def login(request):
	if request.method == "POST":
		res = request.body
		user = UserModel()
		user.fromJson(res)
		fuser = User.objects.filter(name = user.username)
		if len(fuser) == 0:
			return R.badRequest("User does not exist")
		password = fuser[0].password
		md5 = hashlib.md5()
		passwordString = user.password + user.username
		md5.update(passwordString.encode())
		pwd = md5.hexdigest()
		if pwd != password:
			return R.badRequest("password incorrect")
		token = make_token(user)
		return R.ok({"message":"Authorize success","token":token})
	else:
		return R.methodNotAllowed("method not allowed")