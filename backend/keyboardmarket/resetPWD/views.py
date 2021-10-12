from tools.R import R
from users.models import User
import datetime
import json
import hashlib
from tools.emailClient import EmailClient
import jwt

# Create your views here.


def resetPWD(request):
	client = EmailClient()
	if request.method == "POST":
		req = request.body
		data = json.loads(req)
		if "username" not in data:
			return R.badRequest("username does not exist!")
		user = User.objects.filter(name = data["username"])
		if not user:
			return R.badRequest("user not found!")
		token = makeResetToken(user[0])
		username = user[0].name
		user_email = user[0].email
		client.send_reset_message(username,token,user_email)
		return R.ok("reset password request success")
	if request.method == "GET":
		req = request.GET
		if "token" not in req:
			return R.badRequest("token not found")
		token = req["token"]
		username = decodeResetToken(token)
		if type(username) != str:
			return username
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("user not found")
		return R.ok("request is valid")
	if request.method == "PUT":
		req = request.body
		data = json.loads(req)
		if "password" not in data or "token" not in data:
			return R.badRequest("required parameter not found")
		username = decodeResetToken(data["token"])
		if type(username) != str:
			return username
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("User not found")
		user = user[0]
		md5 = hashlib.md5()
		passwordString = data["password"] + username
		md5.update(passwordString.encode())
		pwd = md5.hexdigest()
		user.password = pwd
		user.save()
		return R.ok("update success")

def makeResetToken(user):
	key = "7410828DEA3014679CDF53670B2543E85994D3A9E12596E1BB07DB14B44A6417"
	now = datetime.datetime.now()
	expiretime = now + datetime.timedelta(hours = 1)
	username = user.name
	payload = {
		"username":username,
		"exp":expiretime.timestamp()
	}
	return jwt.encode(payload,key,algorithm = 'HS256')


def decodeResetToken(token):
	key = "7410828DEA3014679CDF53670B2543E85994D3A9E12596E1BB07DB14B44A6417"
	try:
		res = jwt.decode(token,key,algorithms = ['HS256'])
	except jwt.ExpiredSignatureError:
		return R.badRequest("驗證超時，請重新操作!")
	except Exception as e:
		return R.internalServerError(str(e))
	else:
		return res["username"]
