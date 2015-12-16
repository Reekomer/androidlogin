# -*- coding: utf-8 -*


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import ListProperty, Property


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


'''
from kivy.config import Config
Config.set('graphics', 'width', '510')
Config.set('graphics', 'height', '800')
'''



from kivy.core.window import Window


from kivy.lang import Builder
from kivy.uix.screenmanager import (ScreenManager, 
								Screen, 
								SlideTransition,
								SwapTransition,
								FadeTransition,
								WipeTransition)
from kivy.uix.scrollview import ScrollView


#imports for httprequest
import requests
import json
import settings

import login


#CSRF and session data
csrftoken = None
sessionid = None








class ScreenManage(ScreenManager):
	pass










class ScreenHome(Screen):
	pass

class ContainerHome(BoxLayout):
	pass













class KivyApp(App):
	pass



settings.kapp = KivyApp()
if __name__=='__main__':
	settings.kapp.run()



