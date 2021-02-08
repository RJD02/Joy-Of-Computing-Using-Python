'''
Mr. Roxy has arranged a party at his house on the New Year’s Eve. He has invited all his friends - both men and women (men in more number). Your task is to generate the number of ways in which the invitees stand in a line so that no two women stand next to each other. 

Note that the number of men is more than the number of women and Roxy doesn’t invite more than 20 guests.

If there are more than 20 guests or an arrangement as per the given constraints is not possible, print ‘invalid’.


Input Format: 

The first line contains m number of men invited

The second line contains n number of women invited

Note: m +n should not be greater than 20


Output Format: 

Print the number of ways to line up the invitees

Example: 

Input: 
8
5

Output: 
609638400
'''

def factorial(n):
    ret = 1;
    for i in range(1, n + 1):
        ret = ret * i
    return ret

m = int(input())
f = int(input())
if m <= f:
    print('invalid')
else:
    formula = factorial(m + 1) / factorial(m + 1 - f)
    total = factorial(m) * formula
    print(int(total))