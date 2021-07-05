'''
Given a string, remove all the punctuations in it and print only the words in it. 


Input format : 
the input string with punctuations

Output format : 
the output string without punctuations


Example 

input

“Wow!!! It’s a beautiful morning”

 

output

Wow Its a beautiful morning
'''

import string

def solve():
    line = input()
    punct = string.punctuation
    for i in line:
        if i in punct:
            line = line.replace(i, "")
            print(i)
    print(line)
    return

solve()
