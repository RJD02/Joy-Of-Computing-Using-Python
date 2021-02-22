'''
Question:
    Anagrams
Given two strings as input, determine if they are anagrams are not. (Ignore the spaces, case and any punctuation
or special characters)
Note: Anagrams are the strings which are made up of the same set of letters. For example : Mary and Army are 
anagrams.

Input Format

First line of the input contains the first string
Second line of the input contains the second string

Output Format:

Print Yes if the given strings are anagrams, No otherwise.

Example:
Input:
Tom Marvolo Riddle
I am Lord Voldemort!!!

Output:
Yes

'''

import string

punct = string.punctuation
punct += ' '
# print(punct)

def found(char):
    for i in punct:
        if i == char:
            return True
    return False

def main(str1, str2):
    res1 = ""
    res2 = ""
    for i in str1:
        if not found(i):
            res1 += i
    for i in str2:
        if not found(i):
            res2 += i
    res1 = res1.lower(); res2 = res2.lower()
    res1 = ''.join(sorted(res1))
    res2 = ''.join(sorted(res2))
    if len(res1) > len(res2) or len(res1) < len(res2):
        print('No')
        return
    k = 0; count = 0
    for i in res1:
        if i == res2[k]:
            count += 1
        k += 1
    if count == len(res1):
        print('Yes')

str1 = input()
str2 = input()
main(str1, str2)