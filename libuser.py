import settings
import requests

USER_ALREADY_CONNECTED = 1







reqdata = {
	'login-user': None,
	'login-passwd': None
}



class User:
	def __init__(self, username=None, password=None, csrftoken=None, sessionid=None):
		self.username = username
		self.password = password
		self.csrftoken = csrftoken
		self.sessionid = sessionid

	def login(self):
		if self.sessionid:
			return USER_ALREADY_CONNECTED

		reqdata['login-user'] = self.username;
		reqdata['login-passwd'] = self.password;

		res = requests.post(settings.login_url,
							headers=settings.req_headers,
							data=reqdata).json()

		if res['err']:
			return True, res['err']
		else:
			self.sessionid = res['sessionid']
			self.csrftoken = res['csrftoken']
			return False, self.sessionid


	def logout(self):
		pass