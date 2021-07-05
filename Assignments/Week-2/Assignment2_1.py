'''
Write a program in python to read the integer number as input  and print the same.

Input

The input will contain only one number.

Output

Output the same number.

Example

Input

10

Output

10
'''

def check(n):
    if n % 10 != 4:
        return True
    else:
        return False

str = input()

for i in str:
    if i == " ":
        continue
    elif check(int(i)):
        print(int(i), end=" ")
    else:
        continue
