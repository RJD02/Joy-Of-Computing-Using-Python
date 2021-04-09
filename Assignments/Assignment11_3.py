'''
print the number of binary sequences of length ‘n’ that have no consecutive 0’s


Input format : 
A number 'n'

Output format : 
number of binary sequences of length 'n' with no consecutive 0's else invalid




Example 

input

3

output

5


Explanation: 

When n = 3, number of binary digits is 3.

all possible combinations of 3 binary digits are

0 0 0

0 0 1

0 1 0

0 1 1

1 0 0

1 0 1

1 1 0

1 1 1

out of these eight possibilities, 5 have binary sequences and have no consecutive 0’s. 
Hence the number of binary sequences of length 3 is 5.
'''

def solve():
    n = int(input())
    count = 0
    print((n * n + n + 4) // 2)
    return

solve()
