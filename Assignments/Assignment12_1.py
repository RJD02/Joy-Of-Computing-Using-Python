'''
A box is placed at an orientation on the (0,0,0) point. Given other 3 points which are the endpoints. 
Find the volume of the box. 

 

Input format:

line 1 - Point 1 coordinates

line 2 - Point 2 coordinates

line 3 - Point 3 coordinates

 

Output format:

Volume of the box

Example:

Input

2 2 -1

1 3 0

-1 1 4

 
Output

12
'''

def solve():
    p1 = list(map(float, input().split()))
    p2 = list(map(float, input().split()))
    p3 = list(map(float, input().split()))
    d1 = p1[0] * (p2[1] * p3[2] - p2[2] * p3[1])
    d2 = p1[1] * (p2[0] * p3[2] - p2[2] * p3[0])
    d3 = p1[2] * (p2[0] * p3[1] - p2[1] * p3[0])
    res = (d1 - d2 + d3)
    print(abs(res))
    return

solve()
