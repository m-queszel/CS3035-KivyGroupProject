from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class KivyProjApp(App):
    def build(self):
        # AnchorLayout centers its child
        anchor = AnchorLayout(anchor_x='center', anchor_y='center')

        # BoxLayout to stack widgets vertically
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None))
        layout.width = 300  # fixed width
        layout.height = 180  # fixed height

        greetLabel = Label(text="Hello ...!", size_hint=(1, None), height=40)
        userTextField = TextInput(hint_text="Enter your name", multiline=False, size_hint=(1, None), height=40)
        button = Button(text="Say Hello", size_hint=(1, None), height=50)

        def update_label(instance):
            greetLabel.text = f"Hello, {userTextField.text}!"

        button.bind(on_press=update_label)

        # Add widgets to BoxLayout
        layout.add_widget(greetLabel)
        layout.add_widget(userTextField)
        layout.add_widget(button)

        # Add BoxLayout to AnchorLayout
        anchor.add_widget(layout)

        return anchor

if __name__ == "__main__":
    KivyProjApp().run()
