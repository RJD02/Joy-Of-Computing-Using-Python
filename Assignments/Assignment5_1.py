'''
Given an integer input 'n', print a number triangle of n lines as shown in the example.

Input Format

The input contains a number n (n < 10)

Output Format

Print n lines corresponding to the number triangle

Example:

Input

5

Output

1
22
333
4444
55555
'''

def solve(n):
    for i in range(1, n + 1):
        for j in range(0, i):
            print(i, end = "")
        print()
        
solve(int(input()))