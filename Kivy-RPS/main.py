from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from computer import playTurn


class GameLayout(Widget):

    def pressRock(self, instance):
        self.scoreStatus.text = "Rock!"

    def pressPaper(self, instance):
        self.scoreStatus.text = "Paper!"

    def pressScissors(self, instance):
        self.scoreStatus.text = "Scissors!"


class RPSApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return GameLayout()


if __name__ == '__main__':
    RPSApp().run()
