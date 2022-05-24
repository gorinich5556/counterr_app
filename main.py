from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        return Label(text="Hello, World", halign="center")

g = 2
MainApp().run()