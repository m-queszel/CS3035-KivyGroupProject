from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class GameGridLayout(Widget):
    rock = ObjectProperty(None)
    paper = ObjectProperty(None)
    scissors = ObjectProperty(None)
    scoreStatus = ObjectProperty(None)

    def press(self, instance):
        self.scoreStatus.text = "changed!"


class RPSApp(App):
    def build(self):
        return GameGridLayout()


if __name__ == '__main__':
    RPSApp().run()
