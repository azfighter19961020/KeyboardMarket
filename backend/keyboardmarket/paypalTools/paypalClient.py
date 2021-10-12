import os
from paypalcheckoutsdk.core import PayPalHttpClient,SandboxEnvironment

import sys

class PaypalClient:
	def __init__(self):
		self.client_id = os.environ["PAYPAL_CLIENT_ID"] if 'PAYPAL_CLIENT_ID' in os.environ else ""
		self.client_secret = os.environ["PAYPAL_CLIENT_SECRET"] if 'PAYPAL_CLIENT_SECRET' in os.environ else ""
		self.environment = SandboxEnvironment(
			client_id = self.client_id,
			client_secret = self.client_secret
		)
		self.client = PayPalHttpClient(self.environment)