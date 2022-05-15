from tkinter import Widget
from kivy.config import Config

Config.set('graphics', 'width', 720) 
Config.set('graphics', 'height', 1280)

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image

font = './font/Nunito-VariableFont_wght.ttf'

Window.clearcolor = (255, 255, 255, 1)


class MyWidget(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()

ghfgh = 12

        


if __name__ == '__main__':
    MyApp().run()