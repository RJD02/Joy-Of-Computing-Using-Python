'''
Given an array A of N integers, you have to write a python code to eliminate the duplicate integers of the array.

Input Format

The first line of the input contains a number N representing the number of elements in array A.

The second line of the input contains N numbers separated by a space. (after the last element, there is no space)

Output Format

Print the resultant array of elements separated by a space. (no space after the last element)

Example

Input
6
1 2 4 2 5 4

Output
1 2 4 5
'''

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

for i in l:
    print(i, end=" ")
