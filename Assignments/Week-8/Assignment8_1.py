'''
Zero-One Matrix

Given a matrix with M rows and N columns, you are required to check if the matrix is a Zero-One Matrix. A Zero-One or a Binary matrix is a matrix in which all the elements are either 0 or 1.

Input Format
The first line of the input contains two space separated integers M and N which represents the number of rows and the number of columns respectively.
Next M lines represent the elements in M rows with each line containing N space separated integers.

Output Format
Print Yes or No

Example:
Input:
3 3
1 0 0
0 1 0
0 0 1
Output:
Yes

Input:
2 2
1 2
0 1
Output
No

Explanation
In the first case, all the elements of the matrix are 0 and 1. In the second case element at the first row and second column is 2
'''

def solve():
    row, col = input().split(" ")
    row, col = int(row), int(col)
    for i in range(row):
        col_val = input().split(" ")
        col_val = [int(x) for x in col_val]
        for y in col_val:
            if y != 0 and y != 1:
                print('No')
                return
    print('Yes')
    return

def solve():
    row, col = map(int, input().split(" "))
    mat = [list(map(int, input().split())) for i in range(m)]
    for i in range(row):
        for j in range(col):
            if mat[i][j] != 0 and mat[i][j] != 1:
                print('No')
                break
    else:
        print('Yes')
    return

solve()
