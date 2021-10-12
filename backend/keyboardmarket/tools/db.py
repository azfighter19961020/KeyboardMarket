from enum import Enum

class CartStatus(Enum):
	deactivate = 0
	activate = 1

class OrderStatus(Enum):
	deactivate = 0
	notPaid = 1
	paid = 2
	shipping = 3

class ProductStatus(Enum):
	deactivate = 0
	activate = 1

class UserStatus(Enum):
	deactivate = 0
	activate = 1

class FavoriteStatus(Enum):
	deactivate = 0
	activate = 1

class ProductCategory(Enum):
	keyboard = 0
	earphone = 1
	mouse = 2
	desktop = 3

	@staticmethod
	def list():
		return list(map(lambda c: c.value, ProductCategory))

	@staticmethod
	def dict():
		return [
			{"category":"鍵盤","value":ProductCategory.keyboard.value},
			{"category":"耳機","value":ProductCategory.earphone.value},
			{"category":"滑鼠","value":ProductCategory.mouse.value},
			{"category":"桌機","value":ProductCategory.desktop.value}
		]


if __name__ == '__main__':
	print(UserStatus.deactivate.value)
