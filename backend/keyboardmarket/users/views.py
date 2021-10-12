from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from tools.R import R
from tools.models.userModel import UserModel
from tools.token import make_token
import json
import re
import hashlib
from tools.login_check import logincheck
import requests


GOOGLE_RECAPTCHA_API = "https://www.google.com/recaptcha/api/siteverify?secret=%s&response=%s"
secretKey = "6LcMB7kcAAAAAEqQPtwfRk2p20PMbOMhameSwN1l"

@logincheck('PUT','DELETE','GET')
def users(request,username = None):
	if request.method == "POST" and 'avatar' not in request.path:
		res = request.body
		resdata = json.loads(res)
		if "recaptchaToken" not in resdata:
			return R.badRequest("recaptcha token does not exist!")
		recaptchaToken = resdata["recaptchaToken"]
		googleres = requests.post(GOOGLE_RECAPTCHA_API%(secretKey,recaptchaToken))
		googledata = json.loads(googleres.text)
		print(googledata)
		if not googledata["success"]:
			return R.badRequest(googledata["error-codes"])
		user = UserModel()
		user.fromJson(res)
		if not re.match("^[A-Za-z0-9]*$",user.username):
			return R.badRequest("username contains invalid character")
		if not re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',user.email):
			return R.badRequest("email format is not correct")
		if not re.match("^[0-9]*$",user.phone) or len(user.phone) != 10:
			return R.badRequest("phone is not correct")
		if len(user.password) < 6:
			return R.badRequest("password length is not correct")
		if user.password != user.password1:
			return R.badRequest("password verify failed")
		md5 = hashlib.md5()
		passwordString = user.password + user.username
		md5.update(passwordString.encode())
		pwd = md5.hexdigest()
		u = User.objects.create(
				name = user.username,
				password = pwd,
				phone = user.phone,
				address = user.address,
				email = user.email
			)
		u.save()
		token = make_token(user)
		return R.created({"message":"User created","token":token})
	elif request.method == "POST" and 'avatar' in request.path:
		file = request.FILES.get('avatar')
		username = request.POST.get('username')
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("User does not exist")
		user = user[0]
		user.avatar = file
		user.save()
		return R.ok("upload success")
	elif request.method == "PUT":
		res = request.body
		user = UserModel()
		user.fromJson(res)
		fuser = User.objects.filter(name = user.username)
		if not fuser:
			return R.badRequest("User does not exist")
		fuser.update(
			name = user.username,
			phone = user.phone,
			address = user.address
		)
		return R.ok("Update success")
	elif request.method == "GET":
		if username is None:
			return R.badRequest("UserName Not Found")
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("user does not exist")
		user = user[0]
		data = user.toJson()
		return R.ok({"data":data})
	else:
		return R.methodNotAllowed("Method Not Allowed")