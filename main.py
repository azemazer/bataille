import random
import re

print('hello world')

# Initialization

fullGame = []
colors = (' of Hearts', ' of Spades', ' of Diamonds', ' of Clubs' )
numbers = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', )
for i in range(len(colors)):
    for n in range (len(numbers)):
        fullGame.append(numbers[n - 1] + colors[i - 1])

for i in range(len(fullGame)):
    print(fullGame[i - 1])

player1Game = []
player2Game = []

gameState = 'isOver'

# General game purpose functions

def cardValor(card):
    cardWordList = re.sub("[^\w]", " ",  card).split()
    try:
        cardValue = int(cardWordList[0])
    except:
        if cardWordList[0] == 'Jack':
                cardValue = 11
        elif cardWordList[0] == 'Queen':
                cardValue = 12
        elif cardWordList[0] == 'King':
                cardValue = 13
        elif cardWordList[0] == 'Ace':
                cardValue = 14
        else:
             print('Card value error')
    return cardValue
            


# State functions 

def doIsOver():
    global gameState
    global player1Game
    global player2Game

    newGame = input('New game? Y/N')
    if (newGame == 'Y' or newGame == 'y'):
        print('Game On!')
        player1Game = random.shuffle(fullGame)
        player2game = random.shuffle(fullGame)
        gameState = 'isOn'
    elif (newGame == 'N' or newGame == 'n'):
        print('Alright, see you!')
        quit()
    else:
        print('Wrong key! Try again.')

def doIsOn():
    global gameState
    global player1Game
    global player2Game

    player1Cards = drag(player1Game, 1)
    player2Cards = drag(player2Game, 1)

    print('test')
    gameState = 'isOver'


# State loop
while True:
    if gameState =='isOver':
        doIsOver()
    elif gameState == 'isOn':
        doIsOn()