from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons


class MainApp(MDApp):
    icons = {
        'account-circle-outline' : 'account',
        'plus' : 'pllus'
    }

    def build(self):
        return Builder.load_file('app.kv')
    def on_start(self):
        for tab_name in self.icons:
            self.root.ids.tabs.add_widget(Tab(icon=tab_name))

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):

        # get the tab icon.
        count_icon = instance_tab.icon
        # print it on shell/bash.
        print(f"Welcome to '{count_icon} tab'")

class Tab(MDFloatLayout, MDTabsBase):
    pass

MainApp().run()