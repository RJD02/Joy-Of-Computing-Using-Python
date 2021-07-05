'''
Print Matrix
Given an integer N, print a N X N square matrix, consisting of numbers from 1 to N^2, in the row-wise order

Input Format
The first line of the input an integer N

Output Format
Print N lines having numbers from 1 to N^2

Example:
Input:
3
Output:
1 2 3
4 5 6
7 8 9
'''

def solve():
    n = int(input())
    count = 1
    for i in range(n):
        for j in range(n):
            if j == n - 1:
                print(count, end = "")
            else:
                print(count, end = " ")
            count += 1
        print()
    return

solve()
