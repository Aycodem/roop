#!/usr/bin/env python3

import insightface
import roop.globals
import cv2
import numpy as np
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

FACE_ANALYSER = None

class RootWidget(BoxLayout):
    status_label = ObjectProperty(None)
    image_widget = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.init_roop()
        self.load_image()

    def init_roop(self):
        self.face_analyser = None
        self.status_label.text = 'Status: Roop Initialized'

    def load_image(self):
        image_path = 'path/to/your/image.jpg'
        image = cv2.imread(image_path)
        face = get_face_single(image)
        if face:
            face_image = extract_face_from_image(image, face)
            self.image_widget.texture = self.cv_image_to_texture(face_image)

    def cv_image_to_texture(self, cv_image):
        buffer = cv2.flip(cv_image, 0).tostring()
        texture = ImageString(buffer, size=cv_image.shape[:2], colorfmt='bgr')
        texture.flip_vertical()
        return texture

Builder.load_string('''
<RootWidget>:
    orientation: 'vertical'
    StatusLabel:
        id: status_label
        text: 'Status: '
    Image:
        id: image_widget
        size_hint: 1, 1
        allow_stretch: True

<StatusLabel>:
    text: 'Status: '
''')

class StatusLabel(Label):
    pass

def get_face_analyser():
    global FACE_ANALYSER
    if FACE_ANALYSER is None:
        FACE_ANALYSER = insightface.app.FaceAnalysis(name='buffalo_l', providers=roop.globals.providers)
        FACE_ANALYSER.prepare(ctx_id=0, det_size=(640, 640))
    return FACE_ANALYSER

def get_face_single(img_data):
    face = get_face_analyser().get(img_data)
    try:
        return sorted(face, key=lambda x: x.bbox[0])[0]
    except IndexError:
        return None

def extract_face_from_image(image, face):
    x, y, w, h = face.bbox
    face_image = image[y:y+h, x:x+w]
    return face_image

class MyApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MyApp().run()
