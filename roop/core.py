#!/usr/bin/env python3

import os
import sys
import signal
import shutil
import glob
import argparse
import psutil
import cv2

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ObjectProperty

import roop.globals
from roop.swapper import process_video, process_img, process_faces, process_frames
from roop.utils import is_img, detect_fps, set_fps, create_video, add_audio, extract_frames, rreplace
from roop.analyser import get_face_single
import roop.ui as ui

signal.signal(signal.SIGINT, lambda signal_number, frame: quit())
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--face', help='use this face', dest='source_img')
parser.add_argument('-t', '--target', help='replace this face', dest='target_path')
parser.add_argument('-o', '--output', help='save output to this file', dest='output_file')
parser.add_argument('--keep-fps', help='maintain original fps', dest='keep_fps', action='store_true', default=False)
parser.add_argument('--keep-frames', help='keep frames directory', dest='keep_frames', action='store_true', default=False)
parser.add_argument('--all-faces', help='swap all faces in frame', dest='all_faces', action='store_true', default=False)
parser.add_argument('--max-memory', help='maximum amount of RAM in GB to be used', dest='max_memory', type=int)
parser.add_argument('--cpu-cores', help='number of CPU cores to use', dest='cpu_cores', type=int, default=max(psutil.cpu_count() / 2, 1))
parser.add_argument('--gpu-threads', help='number of threads to be use for the GPU', dest='gpu_threads', type=int, default=8)
parser.add_argument('--gpu-vendor', help='choice your GPU vendor', dest='gpu_vendor', choices=['apple', 'amd', 'intel', 'nvidia'])

args = parser.parse_known_args()[0]

if 'all_faces' in args:
    roop.globals.all_faces = True

if args.cpu_cores:
    roop.globals.cpu_cores = int(args.cpu_cores)

# cpu thread fix for mac
if sys.platform == 'darwin':
    roop.globals.cpu_cores = 1

if args.gpu_threads:
    roop.globals.gpu_threads = int(args.gpu_threads)

# gpu thread fix for amd
if args.gpu_vendor == 'amd':
    roop.globals.gpu_threads = 1

if args.gpu_vendor:
    roop.globals.gpu_vendor = args.gpu_vendor
else:
    roop.globals.providers = ['CPUExecutionProvider']

sep = "/"
if os.name == "nt":
    sep = "\\"

Builder.load_string('''
<RootWidget>:
    orientation: 'vertical'
    SelectFaceButton:
        on_release: root.select_face()
    SelectTargetButton:
        on_release: root.select_target()
    ToggleAllFacesButton:
        on_release: root.toggle_all_faces()
    ToggleFpsLimitButton:
        on_release: root.toggle_fps_limit()
    ToggleKeepFramesButton:
        on_release: root.toggle_keep_frames()
    SaveFileButton:
        on_release: root.save_file()
    StartButton:
        on_release: root.start()
    StatusLabel:
        id: status_label
        text: 'Status: '
    ProgressBar:
        value: root.progress_value

<SelectFaceButton>:
    text: 'Select Face Image'

<SelectTargetButton>:
    text: 'Select Target Video/Image'

<ToggleAllFacesButton>:
    text: 'Toggle All Faces'

<ToggleFpsLimitButton>:
    text: 'Toggle FPS Limit'

<ToggleKeepFramesButton>:
    text: 'Toggle Keep Frames'

<SaveFileButton>:
    text: 'Save Output File'

<StartButton>:
    text: 'Start'

<StatusLabel>:
    text: 'Status: '

<ProgressBar>:
    max: 100
    value: 0
''')

class RootWidget(BoxLayout):
    progress_value = NumericProperty(0)

    def select_face(self):
        # Implement select face logic here
        pass

    def select_target(self):
        # Implement select target logic here
        pass

    def toggle_all_faces(self):
        # Implement toggle all faces logic here
        pass

    def toggle_fps_limit(self):
        # Implement toggle fps limit logic here
        pass

    def toggle_keep_frames(self):
        # Implement toggle keep frames logic here
        pass

    def save_file(self):
        # Implement save file logic here
        pass

    def start(self):
        # Implement start logic here
        pass


class SelectFaceButton(Button):
    pass


class SelectTargetButton(Button):
    pass


class ToggleAllFacesButton(ToggleButton):
    pass


class ToggleFpsLimitButton(ToggleButton):
    pass


class ToggleKeepFramesButton(ToggleButton):
    pass


class SaveFileButton(Button):
    pass


class StartButton(Button):
    pass


class StatusLabel(Label):
    pass


class ProgressBar(Label):
    pass


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()
