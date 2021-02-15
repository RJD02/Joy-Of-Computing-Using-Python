'''
Two friends Suresh and Ramesh have m red candies and n green candies respectively. They want to arrange the candies in such a way that each row contains equal number of candies and also each row should have only red candies or green candies. Help them to arrange the candies in such a way that there are maximum number of candies in each row.

Input Format: 

The first line contains m number of red candies Suresh has

The second line contains n number of green candies Ramesh has


Output Format: 

Print maximum number of candies that can be arranges in each row.

Example: 

Input: 
24
18

Output: 
6
'''

def gcd(m, n):
    if m < n:
        m, n = n, m
    if m % n == 0:
        return n
    return gcd(n, m % n)

m = int(input())
n = int(input())
print(gcd(m, n))