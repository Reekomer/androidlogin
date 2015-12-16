
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import ListProperty, Property


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

import popups


class ScreenLogin(Screen):
	pass

class ContainerLogin(AnchorLayout):

	def clean(self):
		self.ids.txt_user.text = ''
		self.ids.txt_password.text = ''

	def login(self):
		tmpusername = self.ids.txt_user.text
		tmppassword = self.ids.txt_password.text

		#string vals
		if not tmpusername.find(' ') < 0 or not tmppassword.find(' ') < 0:
			popups.show_popup(title='Invalid user or password', text='The username or the password that you introduced are invalid')
			return


		#create user and log in
		u = User()
		u.username = self.ids.txt_user.text
		u.password = self.ids.txt_password.text
		
		err, res = u.login()

		#validate successful login
		if err:
			self.clean()
			#popups.show_popup(title='Invalid user or password', text='The username or the password that you introduced are invalid')
			return

		settings.kapp.root.current = 'ScreenHome'





