'''
Repetition
Given a list of integers and a value k, you are required to print an integer which appears in the list exactly k times. It is guaranteed that only one integer repeats k times.
Input Format
The first line of the input contains space separated integers.
Second line of the input contains a value n.
Output Format
Print an integer that appears exactly n times.
Example:
Input:
1 2 3 4 3 2 1 2 5 6
3
Output:
2
Explanation
In the given list, 2 appears exactly thrice.
'''

def solve():
	l = input().split(" ")
	l = [int(x) for x in l]
	k = int(input())
	res = []
	for i in l:
		if i not in res:
			res.append(i)
	d = {i:0 for i in res}
	# print(d)
	for i in l:
		d[i] += 1
	for i in d.keys():
		if d[i] == k:
			print(i)
	return

solve()