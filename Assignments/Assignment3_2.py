def removeRepeated_2(l):
    l1 = l[:]
    l1.reverse()
    l.sort()
    to_remove = []
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            to_remove.append(l[i])
    for i in to_remove:
        l1.remove(i)
    l1.reverse()
    return l1

def sum(l, n):
    l.sort()
    return l[len(l) - n] + l[1]

def giveMeInteger(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def getRepeatedCount(l):
    count = 0
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            count += 1
    return count

def solve(l):
    l.sort()
    min = [l[-1]]#Assign it a list
    max = [l[0]]#Assign it a list
    i = 0
    for i in range(1,len(l)):
        if l[i] > max[len(max) - 1]:
            max.append(l[i])
        if l[i] < min[len(min) - 1]:
            min.append(l[i])
    return max[len(max) - 2] + min[len(min) - 1]

n = input()
l = list(input().split(" "))
l = giveMeInteger(l)
l = removeRepeated_2(l)
print(l)
print(solve(l))
