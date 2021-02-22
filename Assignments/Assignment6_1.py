'''
Question:
Given an integer input 'n', print a palindromic number triangle of n lines as shown in the example.

Input Format

The input contains a number n (n < 10)

Output Format

Print n lines corresponding to the number triangle 

Example:

Input:

5

Output:
Row
1    1
2    121
3    12321
4    1234321
5    123454321

'''
# import random


def solve(n):
    for i in range(1, n + 1):
        k = 1
        for j in range(1, 2 * i):
            if j < i:
                print(k, end="")
                k += 1
            else:
                print(k, end="")
                k -= 1
        print()
    
# Multiple Test case test successful
# Stress test successful.
# while True:
#     n = random.randint(1, 10)
#     print(n)
#     solve(n)
#     # n -= 1
#     print()
n = int(input())
solve(n)