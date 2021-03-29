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
