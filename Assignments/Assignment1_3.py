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


a, b = input().split(" ")
a = int(a)
b = int(b)
if a > b:
    print(a)
else:
    print(b)
