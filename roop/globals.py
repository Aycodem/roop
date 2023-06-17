#!/usr/bin/env python3

import onnxruntime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class RootWidget(BoxLayout):
    status_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.init_roop()

    def init_roop(self):
        self.all_faces = None
        self.log_level = 'error'
        self.cpu_cores = None
        self.gpu_threads = None
        self.gpu_vendor = None
        self.providers = onnxruntime.get_available_providers()

        if 'TensorrtExecutionProvider' in self.providers:
            self.providers.remove('TensorrtExecutionProvider')

        # Update the status label text
        self.status_label.text = f'Status: Initialized Roop with {self.providers}'

Builder.load_string('''
<RootWidget>:
    orientation: 'vertical'
    StatusLabel:
        id: status_label
        text: 'Status: '

<StatusLabel>:
    text: 'Status: '
''')

class StatusLabel(Label):
    pass

class MyApp(App):
    def build(self):
