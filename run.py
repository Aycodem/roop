#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from roop import core

class RootWidget(BoxLayout):
    status_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.init_roop()

    def init_roop(self):
        self.status_label.text = 'Status: Roop Initialized'
        core.run()

class StatusLabel(Label):
    pass

class MyApp(App):
    def build(self):
        return RootWidget() 

if __name__ == '__main__':
    MyApp().run()
