'''
Snakes and Ladders-2
Given a configuration of a Snakes and Ladders board and a series of numbers obtained when the die is rolled,
determine if the sequence of the die rolls lead to a win.

Input Format
First line of the input contains the board configuration in the form of mapping of snakes and ladders
Second line of the input contains comma separated integers indicating the values obtained on rolling a die.

Output Format
Print Yes if the sequence of roll die leads to a winning combination, No otherwise.

Example:Input:
6:  14, 11:  28, 17:  74, 22:  7, 38:  59, 49:  12, 57:  76, 61:  54, 81:  98, 88:  4
6, 3, 4, 3, 2
Output:Yes

Explanation
As per the given configuration, the above set of moves indicate that the winning number 100 is reached.
Hence this is a winning combination.  (It is a winning combination if the set of die rolls lead to a number equal to100 or exceeds 100).
'''

def solve():
    line_input = input().split(",")
    pair = [i.split(":  ") for i in line_input]
    pair = [[int(i[0]), int(i[1])] for i in pair]
    dice = input().split(", ")
    dice = [int(x) for x in dice]
    count = 0
    for i in dice:
        count += i
        for i in pair:
            if i[0] == count:
                count = i[1]
        if count >= 100:
            print('Yes')
            break
    else:
        print('No')

solve()
