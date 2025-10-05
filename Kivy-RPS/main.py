from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class GameLayout(Widget):
    pass

    def press(self, instance):
        self.scoreStatus.text = "changed!"


class RPSApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return GameLayout()


if __name__ == '__main__':
    RPSApp().run()
