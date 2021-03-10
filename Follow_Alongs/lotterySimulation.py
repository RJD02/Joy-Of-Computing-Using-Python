#  You can use infinity in python using float('inf')
import random


def forUser(n):
    account = 0
    for i in range(n):
        bet = int(input('Your bet from 1 to 10'))
        lucky_draw = random.randint(1, 10)
        print(lucky_draw)
        if bet == lucky_draw:
            account += 900 - 100
        else:
            account -= 100
        print(account)
    return

def forMachine(n): 
    account = 0
    for i in range(n):
        bet = random.randint(1, 10)
        lucky_draw = random.randint(1, 10)
        print('Bet ', bet)
        print('Lucky draw:', lucky_draw)
        if bet == lucky_draw:
            account += 900 - 100
        else:
            account -= 100
        print('Amount in your game account:', account)
    return 

n = int(input('Enter the number of times you wanna play this game: '))
choice = input('Do you want to play or automate it?(A-automate, M-Play): ')
if choice == 'A':
    forMachine(n)
else:
    forUser(n)
print('This session ends here')
