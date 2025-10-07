from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from computer import playTurn
from gamelogic import checkWin, displayWinner, displayScore


class Player():
    def __init__(self):
        self.score = 0

    def increaseScore(self):
        self.score = self.score + 1


class GameLayout(Widget):

    player = Player()
    computer = Player()

    def pressRock(self, instance):
        compRoll = playTurn()
        self.computerRoll.text = "You played rock and the computer rolled " + compRoll
        result = checkWin("rock", compRoll, self.player, self.computer)
        self.score.text = displayScore(self.player.score, self.computer.score)
        self.winLabel.text = displayWinner(result)

    def pressPaper(self, instance):
        compRoll = playTurn()
        self.computerRoll.text = "You played paper and the computer rolled " + compRoll
        result = checkWin("paper", compRoll, self.player, self.computer)
        self.score.text = displayScore(self.player.score, self.computer.score)
        self.winLabel.text = displayWinner(result)

    def pressScissors(self, instance):
        compRoll = playTurn()
        self.computerRoll.text = "You played scissors and the computer rolled " + compRoll
        result = checkWin("scissors", compRoll, self.player, self.computer)
        self.score.text = displayScore(self.player.score, self.computer.score)
        self.winLabel.text = displayWinner(result)

    def resetGame(self, instance):
        self.player.score = 0
        self.computer.score = 0
        self.computerRoll.text = "Select your throw!"
        self.score.text = ""
        self.winLabel.text = ""


class RPSApp(App):
    def build(self):
        Window.clearcolor = (240/255, 244/255, 195/255, 1)
        return GameLayout()


if __name__ == '__main__':
    RPSApp().run()
