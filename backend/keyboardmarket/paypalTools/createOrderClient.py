from paypalTools.paypalClient import PaypalClient
from paypalcheckoutsdk.orders import OrdersCreateRequest

RETURN_URL = "http://localhost:8080/#/orderCreated"
CANCEL_URL = "http://localhost:8080/#/orderCanceled"

class CreateOrder(PaypalClient):

	@staticmethod
	def build_request_body(currency_code,value):
		print("currency_code is:",currency_code)
		return \
		{
			"intent":"CAPTURE",
			"application_context":{
				"return_url":RETURN_URL,
				"cancel_url":CANCEL_URL,
				"brand_name":"鍵盤貿易",
				"landing_page":"BILLING",
			},
			"purchase_units":[
				{
					"amount":{
						"currency_code":currency_code,
						"value":value
					}
				}
			]
		}


	def create_order(self,currency_code,value,debug = False):
		request = OrdersCreateRequest()
		request.headers['prefer'] = 'return=representation'
		request.request_body(self.build_request_body(currency_code,value))
		response = self.client.execute(request)
		if debug:
			print("Status code:",response.status_code)
			print("Status:",response.result.status)
			print("Order ID:",response.result.id)
			print("intent:",response.result.intent)
			print("links:")
			for link in response.result.links:
				print("\t{}: {}\tCall Type: {}".format(link.rel,link.href,link.method))
			print("total Amount: {} {}".format(response.result.purchase_units[0].amount.currency_code,
												response.result.purchase_units[0].amount.value))
		return response

