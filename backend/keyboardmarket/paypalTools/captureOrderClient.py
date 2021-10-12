from paypalTools.paypalClient import PaypalClient
from paypalcheckoutsdk.orders import OrdersCaptureRequest

class CaptureOrder(PaypalClient):
	def capture_order(self,order_id,debug = False):
		request = OrdersCaptureRequest(order_id)
		response = self.client.execute(request)
		if debug:
			print("Status code:",response.status_code)
			print("Status:",response.result.status)
			print("Order ID:",response.result.id)
			print("links:")
			for link in response.result.links:
				print("\t{}: {}\tCall Type: {}".format(link.rel,link.href,link.method))
			for purchase_unit in response.result.purchase_units:
				for capture in purchase_units.payments.captures:
					print('\t',capture.id)

		return response