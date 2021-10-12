import jwt
from users.models import User
from tools.R import R

def logincheck(*methods):
	def _logincheck(func):
		def wrapper(request,*args,**kwargs):
			token = request.META.get("HTTP_AUTHORIZATION")
			if request.method not in methods:
				return func(request,*args,**kwargs)
			if not token:
				return R.badRequest("no token")
			try:
				key = '77DA14AA68AAFF38F2A35DA874FA86B88094EE1C60A465ABE85FC84F0CDB6BFF'
				res = jwt.decode(token, key, algorithms=['HS256'])
			except jwt.ExpiredSignatureError:
				return R.badRequest("login again")
			except Exception as e:
				return R.internalServerError("Internal Server Error")
			username = res['username']
			user = User.objects.filter(name = username)
			if not user:
				return R.badRequest("User does not exist")
			request.user = user
			return func(request,*args,**kwargs)
		return wrapper
	return _logincheck