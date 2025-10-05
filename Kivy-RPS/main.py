from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from computer import playTurn
from gamelogic import checkWin, displayWinner


class GameLayout(Widget):

    def pressRock(self, instance):
        compRoll = playTurn()
        self.computerRoll.text = "You played rock and the computer rolled " + compRoll
        result = checkWin("rock", compRoll)
        self.scoreStatus.text = displayWinner(result)

    def pressPaper(self, instance):
        compRoll = playTurn()
        self.computerRoll.text = "You played paper and the computer rolled " + compRoll
        result = checkWin("paper", compRoll)
        self.scoreStatus.text = displayWinner(result)

    def pressScissors(self, instance):
        compRoll = playTurn()
        self.computerRoll.text = "You played scissors and the computer rolled " + compRoll
        result = checkWin("scissors", compRoll)
        self.scoreStatus.text = displayWinner(result)


class RPSApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return GameLayout()


if __name__ == '__main__':
    RPSApp().run()
