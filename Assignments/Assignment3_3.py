def removeRepeated_1(l):
    return list(dict.fromkeys(l))

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

# Why the hell was this given?
# n = int(input())
l = list(input().split(" "))

#For removeRepeated_2
l = removeRepeated_2(l)

#For removeRepeated_1
# l = removeRepeated(l)
for i in l:
    print(i, end=" ")
