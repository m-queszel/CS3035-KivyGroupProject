# Returns 1 if Player wins, returns 0 if computer wins, returns 2 if tie
def checkWin(mainPlayerRoll, computerRoll):
    if mainPlayerRoll == "paper":
        if computerRoll == "paper":
            return 2
        if computerRoll == "rock":
            return 1
        if computerRoll == "scissors":
            return 0

    if mainPlayerRoll == "rock":
        if computerRoll == "rock":
            return 2
        if computerRoll == "paper":
            return 0
        if computerRoll == "scissors":
            return 1

    if mainPlayerRoll == "scissors":
        if computerRoll == "scissors":
            return 2
        if computerRoll == "rock":
            return 0
        if computerRoll == "paper":
            return 1


def displayWinner(num):
    if num == 0:
        return "Computer wins!"
    if num == 1:
        return "You win!"
    if num == 2:
        return "Tie!"
