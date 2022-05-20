from tkinter import Widget
from kivy.config import Config
from kivy.uix.screenmanager import NoTransition

Config.set('graphics', 'width', 720) 
Config.set('graphics', 'height', 1280)

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

font = './font/Nunito-VariableFont_wght.ttf'

Window.clearcolor = (255, 255, 255, 1)


class HelloScreen(Screen):
    pass

class WorkScreen(Screen):
    pass

class CanvasWidget(Widget):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(HelloScreen(name='hello'))
        sm.add_widget(WorkScreen(name='work'))

        return sm

ghfgh = 11




if __name__ == '__main__':
    MyApp().run()