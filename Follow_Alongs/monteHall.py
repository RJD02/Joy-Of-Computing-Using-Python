import random

doors = ['Goat' for _ in range(3)]
goat_door = []
swap = 0 #  Number of swap wins
dont_swap = 0 #  Number of don't swap wins
j = 0
while(j < 10):
    x = random.randint(0, 2) #  xth door will comprise of BMW
    doors[x] = "BMW"
    for i in range(3):
        if i == x:
            continue
        else:
            goat_door.append(i)

    choice = int(input('Enter your choice: '))
    door_open = random.choice(goat_door) #  Open a door which has goat behind it
    while(door_open == choice): #  Door opened shouldn't be equal to choice made by participant
        door_open = random.choice(goat_door)

    ch = input('Do you want to swap y-yes, n-no')
    if(ch == 'y'):
        if doors[choice] == 'Goat':
            print('Player wins')
            swap += 1
        else:
            print('Player lost')
    else:
        if doors[choice] == 'Goat':
            print('Player lost')
        else:
            print('Player wins')
            dont_swap += 1
    j += 1

print(swap)
print(dont_swap)
