'''
Given n – indicating the number of rows, print a right angle triangle of squares of numbers with n rows.

Example: 

n = 3

Right angle triangle is

1 
4 9 
16 25 36 


Input Format: 

The first line contains n number of rows


Output Format: 

Print the right-angle triangle of n rows

Example: 

Input: 
4

Output: 

1 
4 9 
16 25 36 
49 64 81 100 


'''

def solve(n):
    sq = 1
    for i in range(1, n + 1):
        for j in range(0, i):
            print(sq * sq,end = " ")
            sq += 1
        print()

n = int(input())
solve(n)