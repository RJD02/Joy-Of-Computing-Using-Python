'''
Snakes and Ladders-1
Given a configuration of a Snakes and Ladders board, determine the number of snakes and ladders.

Input Format
First line of the input contains the board configuration in the form of mapping of snakes and ladders

Output Format
Print two space separated integers indicating the number of snakes and ladders respectively.

Example:
Input: 
6: 14,11: 28,17: 74,22: 7,38: 59,49: 12,57: 76,61: 54,81: 98,88: 4

Output:
4 6

Explanation
In the given configuration, 6:14 indicates a ladder and 22:7 indicates a snake. there are 4 snakes and 6 ladders.
'''

def solve():
    count_snakes = 0
    count_ladders = 0
    line = input().split(",")
    c = []
    for i in line:
        c.append(i.split(":"))
    for i in c:
        i[0] = int(i[0])
        i[1] = int(i[1])
    for i in c:
        if i[0] < i[1]:
            count_ladders += 1
        elif i[0] > i[1]:
            count_snakes += 1
    print(count_snakes,count_ladders)

solve()
