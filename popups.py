from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView



from kivy.properties import StringProperty


popup = None







class MessageBox(ScrollView):
	pass



def show_popup(title='Android message',
			text='Android message'):
	msgbox = MessageBox()
	for i in xrange(1000):
		msgbox.text += str(i)+ ' '

	btn = Button(text='OK')
	btn.font_size = 35
	btn.size_hint_y = None
	btn.height = 100
	btn.on_release = hide_popup

	b = BoxLayout()
	b.orientation = 'vertical'
	b.add_widget(msgbox)
	b.add_widget(btn)

	global popup
	popup = Popup(title=title,
				content=b,
	      		auto_dismiss=False)
	
	popup.open()



def hide_popup():
	global popup
	if popup:
		popup.dismiss()
