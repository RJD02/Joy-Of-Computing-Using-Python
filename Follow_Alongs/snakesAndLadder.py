from PIL import Image
import random
end = 100

def result(pl1_name, pl2_name, points1, points2): #  Shows end result of player 1 and 2
    print(pl1_name, 'scored', points1)
    print(pl2_name, 'scored', points2)
    print('Quitting the game, Thanks for playing')
    return


def showBoard():
    img = Image.open('snakes_and_ladders_image.png')
    img.show()
    return

def l():
    print('Climbing up a ladder')
    return

def s():
    print('Oh no Snake!')
    return

def checkLadder(points):
    if points == 1:
        l()
        return 38
    if points == 4:
        l()
        return 14
    if points == 8:
        l()
        return 30
    if points == 28:
        l()
        return 76
    if points == 21:
        l()
        return 42
    if points == 50:
        l()
        return 67
    if points == 71:
        l()
        return 92
    if points == 88:
        l()
        return 99
    return points #  Not a ladder

def checkSnake(points):
    if points == 32:
        s()
        return 10
    if points == 36:
        s()
        return 6
    if points == 48:
        s()
        return 26
    if points == 62:
        s()
        return 18
    if points == 88:
        s()
        return 24
    if points == 95:
        s()
        return 56
    if points == 97:
        s()
        return 78
    return points #  Not a snake

def reachedEnd(points):
    return points == end

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
                result(pl1_name, pl2_name, points1, points2)
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
                result(pl1_name, pl2_name, points1, points2)
                break
        else:
            print(pl2_name," it's your turn")
            #  Ask player whether player wants to continue
            c = int( input('Enter 1 to continue, 0 to quit'))
            if c == 0:
                result(pl1_name, pl2_name, points1, points2)
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
                result(pl1_name, pl2_name, points1, points2)
                break
        turn += 1



showBoard()
play()
