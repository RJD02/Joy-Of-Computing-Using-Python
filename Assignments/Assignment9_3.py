'''
Remove Vowels
Given a string s, remove all the vowels in s and reprint the string. The order of other characters in the string should be maintained\\

Input Format
A single line of the input contains a stirng s.

Output Format
Print the modified string after removing the vowels

Example:

Input:
abcdEfghi

Output:
bcdfgh
'''

def solve():
	line = input()
	res = ""
	for i in line:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
			continue
		res += i
	print(res)

solve()