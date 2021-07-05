'''
Given a list A of numbers (integers), you have to print those numbers which are not ending with 4.

Input Format

The first line contains numbers separated by a space.

Output Format

Print the resultant array elements separated by a space. (no space after the last element)

Example

Input

2 3 5 4 7 12 14 13 24 40 14

Output

2 3 5 7 12 13 40
'''


def solve():
	l = list(input().split(" "))
	for i in range(len(l)):
	    l[i] = int(l[i])
	    if abs(l[i]) % 10 != 4:
	        print(l[i], end=" ")
	return

solve()
