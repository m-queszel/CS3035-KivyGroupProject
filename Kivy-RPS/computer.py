import random


def rollNum():
    return random.randint(1, 3)


def playTurn():
    num = rollNum()
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    else:
        return "scissors"
