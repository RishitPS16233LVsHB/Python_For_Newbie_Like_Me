import random

def lucky_draw():
    return random.randint(1, 600)

winner = lucky_draw()
print("The winner of the lucky draw is ticket number:", winner)
