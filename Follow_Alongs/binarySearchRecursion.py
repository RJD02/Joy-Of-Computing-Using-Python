# Binary Search using Recursion
def binarySearch(A, key, start, end):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if A[mid] < key:
        return binarySearch(A, key, mid + 1, end)
    elif A[mid] > key:
        return binarySearch(A, key, start, mid - 1)
    elif A[mid] == key:
        return mid
    
# l = [x for x in range(1, 10000000)]
l = list(input().split(" "))
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
key = int(input())
print('Sorted list is:', l, '\nValue', key, 'is at position')
if binarySearch(l, key, 0, len(l)) == -1:
    print("Value doesn't exist in the list")
else:
    print(1 + binarySearch(l, key, 0, len(l)))
    