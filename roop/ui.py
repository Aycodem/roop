from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.slider import Slider

class PreviewWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        # Preview image
        self.preview_image = Image()

        # Preview frame slider
        self.preview_frame_slider = Slider(min=0, max=0, value=0)

        # Test button
        self.test_button = Button(text="Test", background_color=(0.95, 0.76, 0.06, 1))
        
        # Add widgets to layout
        self.add_widget(self.preview_image)
        self.add_widget(self.preview_frame_slider)
        self.add_widget(self.test_button)

class MyApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=[10, 10, 10, 10], spacing=10)

        # Contact information
        support_label = Label(text="Donate to project <3", color=(0.99, 0.47, 0.66, 1))
        layout.add_widget(support_label)

        # Left frame
        left_frame = BoxLayout(orientation='vertical', size_hint=(0.4, None), height=180)
        face_label = Image()
        left_frame.add_widget(face_label)
        layout.add_widget(left_frame)

        # Right frame
        right_frame = BoxLayout(orientation='vertical', size_hint=(0.4, None), height=180)
        target_label = Image()
        right_frame.add_widget(target_label)
        layout.add_widget(right_frame)

        # Select a face button
        face_button = Button(text="Select a face", background_color=(0.45, 0.52, 0.58, 1))
        layout.add_widget(face_button)

        # Select a target button
        target_button = Button(text="Select a target", background_color=(0.45, 0.52, 0.58, 1))
        layout.add_widget(target_button)

        # All faces checkbox
        all_faces_checkbox = CheckBox(active=False)
        layout.add_widget(all_faces_checkbox)

        # FPS limit checkbox
        fps_checkbox = CheckBox(active=True)
        layout.add_widget(fps_checkbox)

        # Keep frames checkbox
        frames_checkbox = CheckBox(active=False)
        layout.add_widget(frames_checkbox)

        # Start button
        start_button = Button(text="Start", background_color=(0.95, 0.76, 0.06, 1))
        layout.add_widget(start_button)

        # Preview button
        preview_button = Button(text="Preview", background_color=(0.95, 0.76, 0.06, 1))
        layout.add_widget(preview_button)

        # Status label
        status_label = Label(text="Status: waiting for input...", color=(0.18, 0.80, 0.44, 1))
        layout.add_widget(status_label)

        return layout

if __name__ == '__main__':
    MyApp().run()
