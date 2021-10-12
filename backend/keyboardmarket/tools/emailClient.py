from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

class EmailClient:
	def __init__(self):
		self.EMAIL_HOST_USER = settings.EMAIL_HOST_USER

	def send_order_message(self,
							username,
							orderno,
							products,
							created_time,
							status,
							user_email):
		email_template = render_to_string(
			'orders/createorder.html',
			{
				"username":username,
				"orderno":orderno,
				"products":products,
				"created_time":created_time,
				"status":status
			}
		)

		email = EmailMessage(
			"鍵盤貿易 - 訂單建立成功通知信",
			email_template,
			self.EMAIL_HOST_USER,
			[user_email]
		)
		email.content_subtype = 'html'
		email.fail_silently = False
		email.send()

	def send_reset_message(self,
							username,
							token,
							user_email):
		email_template = render_to_string(
			'reset/resetpassword.html',
			{
				"username":username,
				"token":"http://localhost:8080/#/reset?token=" + token
			}
		)

		email = EmailMessage(
			"鍵盤貿易 - 重設密碼通知信",
			email_template,
			self.EMAIL_HOST_USER,
			[user_email]
		)
		email.content_subtype = 'html'
		email.fail_silently = False
		email.send()


