from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class rpsGame(Widget):
    pass


class RPSApp(App):
    def build(self):
        return rpsGame()


if __name__ == '__main__':
    RPSApp().run()
