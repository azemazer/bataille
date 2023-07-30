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

player1Cards = []
player2Cards = []

gameState = 'isOver'
duelState = 'isOver'

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

def drag(gameOfCards, numberOfCards):
    currentCards = []
    currentGameOfCards = gameOfCards
    for i in range (numberOfCards):
        currentCards.append(gameOfCards[-1])
        currentGameOfCards.remove(gameOfCards[-1])
    return currentCards
          
            


# State functions 

def doGameIsOver():
    global gameState
    global player1Game
    global player2Game

    newGame = input('New game? Y/N')
    if (newGame == 'Y' or newGame == 'y'):
        print('Game On!')
        player1Game = fullGame
        random.shuffle(player1Game)
        player2Game = fullGame
        random.shuffle(player2Game)
        gameState = 'isOn'
    elif (newGame == 'N' or newGame == 'n'):
        print('Alright, see you!')
        quit()
    else:
        print('Wrong key! Try again.')

def doGameIsOn():
    global gameState
    global duelState
    global player1Game
    global player2Game

    global player1Cards
    global player2Cards

    if duelState == 'isOver':
        if not player1Game:
            print("player 2 won!")
            gameState = 'isOver'
        elif not player2Game:
            print("player 1 won!")
            gameState = 'isOver'
        else:
            random.shuffle(player1Game)
            random.shuffle(player2Game)
            player1Cards = drag(player1Game, 1)
            player2Cards = drag(player2Game, 1)
            duelState = 'isOn'

    elif duelState == 'isOn':

        if cardValor(player1Cards[-1]) > cardValor(player2Cards[-1]):
            player1Game += player2Cards
            print("Player 1 won the cards: ")
            for i in range (len(player2Cards)):
                print (player2Cards[i])
                player2Game.remove(player2Cards[i])
                print ("Player 2 has " + str(len(player2Game)) + " cards left")
            duelState = 'isOver'

        elif cardValor(player2Cards[-1]) > cardValor(player1Cards[-1]):
            player2Game += player1Cards
            print("Player 2 won the cards: ")
            for i in range (len(player1Cards)):
                print (player1Cards[i])
                player1Game.remove(player1Cards[i])
                print ("Player 1 has " + str(len(player1Game)) + " cards left")
            duelState = 'isOver'

        elif cardValor(player2Cards[-1]) == cardValor(player1Cards[-1]):
            print("Bataille between two " + player2Cards[-1] + " !")
            player1Cards += drag(player1Game, 2)
            player2Cards += drag(player2Game, 2)
         


# State loop
while True:
    if gameState =='isOver':
        doGameIsOver()
    elif gameState == 'isOn':
        doGameIsOn()