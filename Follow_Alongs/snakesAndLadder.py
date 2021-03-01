from PIL import Image
import random
end = 100

def result(): #  Shows end result of player 1 and 2
    print(pl1_name, 'scored', points1)
    print(pl2_name, 'scored', points2)
    print('Quitting the game, Thanks for playing')


def showBoard():
    img = Image.open('snakes_and_ladders_image.png')
    img.show()


def play():
    #  Asking players for their name
    pl1_name = input('Enter player 1 name: ')
    pl2_name = input('Enter player 2 name: ')
    points1 = 0 #  Initial points for player 1
    points2 = 0 #   Initial points for player 1
    turn = 0

    while(1):
        if turn % 2 == 0: #  Player 1 turn
            print(pl1_name, "it's your turn")
            #  Ask player whether player wants to continue
            c = int( input('Enter 1 to continue, 0 to quit'))
            if c == 0:
                result()
                break
            #  Generate a random number representing, rollin of a dice
            dice = random.randint(1, 6)
            print('Dice showed: ', dice)
            points1 += dice
            points1 = checkLadder(points1)
            points1 = checkSnake(points1)
            if points1 > end:
                points1 = end
            print(pl1_name, 'your score is: ', points1)
            if reachedEnd(points1):
                print(pl1_name, 'won')
                result()
                break
        else:
            print(pl1_name," it's your turn")
            #  Ask player whether player wants to continue
            c = int( input('Enter 1 to continue, 0 to quit'))
            if c == 0:
                result()
                break
            #  Generate a random number representing, rollin of a dice
            dice = random.randint(1, 6)
            print('Dice showed: ', dice)
            points2 += dice
            points2 = checkLadder(points2)
            points2 = checkSnake(points2)
            if points2 > end:
                points2 = end
            print(pl1_name, 'your score is: ', points2)
            if reachedEnd(points2):
                print(pl2_name, 'won')
                result()
                break
        turn += 1



showBoard()
play()
