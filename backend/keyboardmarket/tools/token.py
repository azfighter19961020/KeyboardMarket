import jwt
import time

def make_token(data):
	key = "77DA14AA68AAFF38F2A35DA874FA86B88094EE1C60A465ABE85FC84F0CDB6BFF"
	now = time.time()
	expiretime = 60 * 60
	payload = {
		"username": data.username,
		"expire": now + expiretime
	}
	return jwt.encode(payload,key,algorithm = 'HS256')
