"""
The alphabets are enumerated as A = 0, B = 1, C = 2, ... , Z = 25.
Consider an encryption scheme where a character with value Ci in the plaintext is replaced by another
character with value Cj using the formula Cj = (Ci + 5) % 26. After replacement,
the resulting string is shuffled (permuted) at random to obtain the cipher text.

Given a plain text and a possible cipher text,
your task is to determine whether the cipher text can be formed from the plain text using the above mentioned scheme.

(Assume that all the strings are in uppercase)

Input Format:

The first line of the input contains a string indicating the plain text.

The second line of the input a string indicating a possible cipher text

Output Format:

Display Yes or No (no newline after the output)

Example:

Input:

PYTHON
TDMSUY

Output:

Yes

Input:

JOCPNPTEL
JQYVSUTHO

Output:

No
"""

def solve():
    x=input()
    y=input()
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    t=''
    for i in x:
        c=a.index(i)
        cj=(c+5)%26
        t=t+a[cj]
    if(sorted(y)==sorted(t)):
        print("Yes",end='')
    else:
        print("No",end='')
    return

solve()