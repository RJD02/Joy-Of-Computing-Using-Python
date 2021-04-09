'''
Let ‘n’ be a positive even integer. Print the total number of ways to express ‘n’ as a sum of only even positive integers. 

Input format :
The positive even integer
Output format :
the total number of ways to express ‘n’ as a sum of only even positive integers else invalid

Example 
input
6
 
output
4

Explanation: There only 4 ways to express ‘6’ as sum of even integers:
First way:  6
Second way: 2 + 4
Third way:  4 + 2
Fourth way: 2 + 2 + 2 + 2
'''

def solve():
    n = int(input())
    if n % 2 == 1:
        print('invalid')
        return
    ways = [1 for _ in range(n // 2)]
    for i in range(1, n // 2):
        ways[i] = 2 * ways[i - 1]
    print(ways[n // 2 - 1])
    return

solve()
