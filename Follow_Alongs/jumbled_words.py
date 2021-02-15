import random

def jumble(word):
    jumbled_word = "".join(random.sample(word, len(word)))
    #For even length of word choose odd multiple to traverse.
    #For odd length of word choose even multiple to traverse.
    return jumbled_word

def choose():
    words = ['hello', 'welcome', 'howdy', 'Good', 'computer', 'Joy', 'computing', 'python', 'programming']
    return random.choice(words)

def thanks(p1_name, p2_name, p1_points, p2_points):
    print(p1_name, "Your final points are", p1_points)
    print(p2_name, "Your final points are", p2_points)
    print(p1_name, "&", p2_name, "Thanks for playing")

def play():
    p1_name = input('Enter player 1 name:')
    p2_name = input('Enter player 2 name:')
    p1_points = 0
    p2_points = 0
    turn = 0
    #create a list of words and store a bunch of words.
    while 1:
        picked_word = choose()
        qn = jumble(picked_word)
        # picked_word = "Hello"
        # qn = "Hello"
        print(qn)
        if turn == 0:
            turn = 1
            print(p1_name, "It's your turn")
            ans = input('What\'s on my mind?')
            if ans == picked_word:
                p1_points += 1
                print('Congrats!! Your score now is:', p1_points)
            else:
                print('Better luck next time, I thought', picked_word)
        else:
            turn = 0
            print(p2_name, "It's your turn")
            ans = input("What's on my mind?")
            if ans == picked_word:
                p2_points += 1
                print('Congrats!! Your score now is', p2_points)
            else:
                print('Better luck next time, I thought', picked_word)
        ans = int(input('Enter 1 to continue and 0 to stop: '))
        if ans == 0:
            thanks(p1_name, p2_name, p1_points, p2_points)
            break
    return

play()
