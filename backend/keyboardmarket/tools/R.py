from django.http import JsonResponse

# status code: 200 OK
STATUS_OK = 200

# status code 201 : created
CREATED = 201

# status code 401 : Unauthorized
UNAUTHORIZED = 401

# status code: 400 Bad Request
BAD_REQUEST = 400

# status code: 405 method not allowed
METHOD_NOT_ALLOWED = 405

# status code: 500 Internal Server Error
INTERNAL_SERVER_ERROR = 500

class R:
	@staticmethod
	def ok(data = None):
		if data is None:
			return JsonResponse({"code":STATUS_OK})
		return JsonResponse({"code":STATUS_OK,"data":data})

	@staticmethod
	def created(data = None):
		if data is None:
			return JsonResponse({"code":CREATED})
		return JsonResponse({"code":CREATED,"data":data})

	@staticmethod
	def unauthorized(data = None):
		if data is None:
			return JsonResponse({"code":UNAUTHORIZED})
		return JsonResponse({"code":UNAUTHORIZED,"data":data})

	@staticmethod
	def badRequest(data = None):
		if data is None:
			return JsonResponse({"code":BAD_REQUEST})
		return JsonResponse({"code":BAD_REQUEST,"data":data})

	@staticmethod
	def methodNotAllowed(data = None):
		if data is None:
			return JsonResponse({"code":METHOD_NOT_ALLOWED})
		return JsonResponse({"code":METHOD_NOT_ALLOWED,"data":data})

	@staticmethod
	def internalServerError(data = None):
		if data is None:
			return JsonResponse({"code":INTERNAL_SERVER_ERROR})
		return JsonResponse({"code":INTERNAL_SERVER_ERROR,"data":data})


if __name__ == "__main__":
	print(R.internalServerError("server is busy"))
