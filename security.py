from werkzeug.security import safe_str_cmp
from models.user import UserModel

# Below function gets invoked whenever the user requests ../auth
def authenticate(username, password):
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user

#Below function gets invoked whenever the user requests an end point to be authhenticated
def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)
