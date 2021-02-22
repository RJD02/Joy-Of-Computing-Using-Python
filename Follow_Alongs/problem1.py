'''
Nandini has a complex matrix script. The matrix script is a N X M grid of strings. It consists of alphanumeric
characters and symbols (!,@,#,$,%,&). To decode the script, Nandini needs to read each column and select only the
alphanumeric characters and connect them. She reads the column from top to bottom and starts reading from the
leftmost column. If there are symbols in the decoded script, then Nandini removes them for better readability. 
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
'''

n, m = map(int, input().split())
l = []
for i in range(n):
    try:
        for j in range(m):
            l.append(list(map(str, input().split())))
    except EOFError:
        break
res = ""
for i in range(m):
    for j in range(n):
        if l[j][i].isalnum():
            # res append(l[j][i])
            print(l[j][i], end = "")

# print(str(res))
"""
7 3
T s i
h % x
i  # $
s M #
$ a  &
# t %
i r !
"""