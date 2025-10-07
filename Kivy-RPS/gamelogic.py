# Returns 1 if Player wins, returns 0 if computer wins, returns 2 if tie

def checkWin(mainPlayerRoll, computerRoll, player, computer):
    if mainPlayerRoll == "paper":
        if computerRoll == "paper":
            return 2
        if computerRoll == "rock":
            player.increaseScore()
            return 1
        if computerRoll == "scissors":
            computer.increaseScore()
            return 0

    if mainPlayerRoll == "rock":
        if computerRoll == "rock":
            return 2
        if computerRoll == "paper":
            computer.increaseScore()
            return 0

        if computerRoll == "scissors":
            player.increaseScore()
            return 1

    if mainPlayerRoll == "scissors":
        if computerRoll == "scissors":
            return 2
        if computerRoll == "rock":
            computer.increaseScore()
            return 0

        if computerRoll == "paper":
            player.increaseScore()
            return 1


def displayWinner(num):
    if num == 0:
        return "Computer wins!"
    if num == 1:
        return "You win!"
    if num == 2:
        return "Tie!"


def displayScore(humanScore, computerScore):
    return "Your score: " + str(humanScore) + " | Computer score: " + str(computerScore)
