'''
Question:
    Break the Secret

You are hired by a secret service agency. Your job is to decode messages. You figure out the algorithm used to 
encrypt messages and it turns out to be as follows:
The message will consist of only uppercase alphabets. The positional values are assigned to the characters as 
A=0, B=1, ..., Y=24 and Z=25. In the original message, a character at position i is replaced by a character using 
the shift formula (i+3)%26.
For example A will be replaced by D, B by E an so on. After replacement, the string is reversed and sent as a 
message.
You are required to decode this message through your code.(Assuming No Space in the message)

Input Format

A single line of the input contains the encrypted message

Output Format

Print a string containing the original message after decoding

Example:

Input

HBEGRRJ

Output:

GOODBYE
'''

def main(str1):
    # str1 =I "".join(reversed(str1))
    str2 = ""
    for i in str1:
        str2 += chr((ord(i) - 3 + 65) % 26 + 65)
    print(str2)
    

str1 = input()
str1 = "".join(reversed(str1))
main(str1)