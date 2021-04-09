'''
List Prefix
Given two lists, write a program to check if one list is a prefix of the other.

Input Format
The first line contains space separated integers
The second line contains space separated integers

Output Format
Print Yes or No

Example:
Input:
1 2
1 2 3 2 1
Output
Yes

Input:
1 2
1 3 2 1
Output:
No

Explanation
 In the first case, first list is a prefix of the second list. In the second case first list is not a prefix of the second
'''

def solve():
    l1 = input().split(" ")
    l2 = input().split(" ")
    l1 = [int(x) for x in l1]
    l2 = [int(x) for x in l2]
    count_l2 = 0
    for i in l1:
        if i != l2[count_l2]:
            print('No')
            break
        count_l2 += 1
    else:
        print('Yes')


solve()
