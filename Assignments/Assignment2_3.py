'''
Given two integer numbers as input, print the larger number.

Input format:

The first line of input contains two numbers separated by a space

Output Format:

Print the larger number

Example

Input

2 3

Output

3
'''

def solve():
	i, j = input().split(" ")
	i, j = int(i), int(j)
	if i < j:
		print(j)
	else:
		print(i)
	return

solve()