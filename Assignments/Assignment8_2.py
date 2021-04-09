'''
Symmetric Matrix

Given a N X N square matrix, determine if it is a Symmetric Matrix.

Input Format
The first line of the input an integer N which represents the number of rows and the number of columns.
Next N lines represent the elements of the matrix.

Output Format
 Print Yes or No

Example:
Input:
3
1 -2 3
-2 3 1
3 1 2
Output:
Yes
'''

def solve():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input().split(" "))
    l = [[int(x) for x in l[i]] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if l[i][j] != l[j][i]:
                print('No')
                return
    print('Yes')
    return

solve()
