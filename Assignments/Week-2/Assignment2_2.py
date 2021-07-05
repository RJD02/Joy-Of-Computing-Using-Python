'''
Write a program to multiply given two integers and display the result.

Input format:

The first line of the input contains two numbers separated by a space

Output Format:

Print the result in single line

Example:

Input

4 2

Output

8
'''

def solve():
	i, j = input().split()
	i, j = int(i), int(j)
	print(i * j)
	return

solve()