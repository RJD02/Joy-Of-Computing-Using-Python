'''
You are given some words. Some of them may repeat. For each word, output its number of occurrences. The output 
order should correspond with the input order of appearance of the word. See the sample input/output for 
clarification.
Sample Input:
bcdef abcdefg bcde bcdef
Sample Output:
3 211
'''

li = input().split()
d = dict()
for i in li:
    d[i] = d.get(i, 0) + 1
print(len(d), end = " ")
for i in d.values():
    print(i, end = " ")