from tools.R import R
from tools.login_check import logincheck
from usercart.models import Cart
from users.models import User
from .models import Order
import json
import uuid
import datetime
from tools.db import CartStatus,OrderStatus
from paypalTools.createOrderClient import CreateOrder
from paypalTools.captureOrderClient import CaptureOrder
from tools.emailClient import EmailClient

CURRENCY_CODE = "TWD"

@logincheck('POST','GET')
def userorder(request,orderno = None):
	if request.method == "GET" and orderno:
		req = request.GET
		if "username" not in req:
			return R.badRequest("username not found")
		username = req["username"]
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("user does not exist")
		user = user[0]
		userorder = Order.objects.filter(user = user).filter(orderno = orderno)
		if not userorder:
			return R.badRequest("order does not exist")

		data = {}
		for order in userorder:
			if "orderno" not in data:
				product = order.product.toJson()
				product["amount"] = order.amount
				product["subtotal"] = order.amount * product["price"]
				data = {
					"id":order.id,
					"orderno":order.orderno,
					"products":[
						product
					],
					"username":order.user.name,
					"address":order.user.address,
					"amount":order.amount,
					"paypal_id":order.paypal_id,
					"created_time":order.created_time,
					"modified_time":order.modified_time,
					"orderStatus":order.status,
					"phone":order.user.phone,
				}
			else:
				product = order.product.toJson()
				product["amount"] = order.amount
				product["subtotal"] = order.amount * product["price"]
				data["products"].append(
					product
				)
				data["amount"] += order.amount
			print(data)
		return R.ok(data)

	if request.method == "GET":
		req = request.GET
		if "username" not in req:
			return R.badRequest("username not found")
		username = req["username"]
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("user does not exist")
		user = user[0]
		userorder = Order.objects.filter(user = user)

		data = []
		for order in userorder:
			for d in data:
				if order.orderno == d["orderno"]:
					d["products"].append(order.product.toJson())
					d["amount"] += order.amount
					break
			else:
				data.append({
					"orderno":order.orderno,
					"products":[
						order.product.toJson()
					],
					"username":order.user.name,
					"amount":order.amount,
					"status":order.status,
					"paypal_id":order.paypal_id,
					"created_time":order.created_time,
					"modified_time":order.modified_time
				})
		return R.ok({"data":data})

	if request.method == "POST":
		req = request.body
		udata = json.loads(req)
		if "username" not in udata:
			return R.badRequest("username not found")
		username = udata["username"]
		user = User.objects.filter(name = username)
		if not user:
			return R.badRequest("user does not exist")
		user = user[0]
		usercart = Cart.objects.filter(user = user).filter(status = CartStatus.activate.value)
		if not usercart:
			return R.badRequest("cart is empty")
		now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		uuid4String = str(uuid.uuid4()).split("-")[0]
		orderno = now + uuid4String
		totalvalue = 0
		for cart in usercart:
			totalvalue += cart.amount * cart.product.price
		try:
			paypalresponse = CreateOrder().create_order(CURRENCY_CODE,totalvalue)
		except Exception as e:
			return R.internalServerError(str(e))
		else:
			data = fromPaypalResponse(paypalresponse)
			paypal_id = data["orderid"]
			products = []
			for cart in usercart:
				cart.status = CartStatus.deactivate.value
				cart.save()
				userorder = Order.objects.create(
					orderno = orderno,
					product = cart.product,
					user = cart.user,
					amount = cart.amount,
					status = OrderStatus.notPaid.value,
					paypal_id = paypal_id
				)	
				products.append(cart.product)

			user_email = user.email
			created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			status = OrderStatus.notPaid.value

			client = EmailClient()
			client.send_order_message(
				user.name,
				orderno,
				products,
				created_time,
				status,
				user_email
			)
			return R.ok(data)
		
	else:
		return R.methodNotAllowed('method not allowed')


def fromPaypalResponse(response):
	data = {}
	data["code"] = response.status_code
	data["status"] = response.result.status
	data["orderid"] = response.result.id
	data["intent"] = response.result.intent
	data["links"] = {}
	for link in response.result.links:
		data["links"][link.rel] = link.href
	data["total_Amount"] = response.result.purchase_units[0].amount.value
	return data


@logincheck('POST')
def captureOrder(request,orderID = None):
	if not orderID:
		return R.badRequest("order id does not exist")
	if request.method == "POST":
		try:
			response = CaptureOrder().capture_order(orderID)
		except Exception as e:
			return R.internalServerError(str(e))
		else:
			orders = Order.objects.filter(paypal_id = orderID)
			for order in orders:
				order.status = OrderStatus.paid.value
				order.save()
			return R.ok(fromCaptureResponse(response))
	else:
		return R.methodNotAllowed("method not allowed")

def fromCaptureResponse(response):
	data = {}
	data["code"] = response.status_code
	data["status"] = response.result.status
	data["orderid"] = response.result.id
	data["links"] = {}
	for link in response.result.links:
		data["links"][link.rel] = link.href
	data["capture"] = []
	for purchase_unit in response.result.purchase_units:
		for capture in purchase_unit.payments.captures:
			data["capture"].append(capture.id)
	return data