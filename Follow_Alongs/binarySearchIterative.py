# Binary Search using iterative search
def binarySearch(A, key):
    start = 0; end = len(A)
    for i in range(start, end):
        mid = (start + end) // 2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# l = [x for x in range(1, 10)]
l = list(input().split(" "))
for i in range(len(l)):
    l[i] = int(l[i])
# print(l)
key = int(input())
print('Value', key, 'in array')
l.sort()
print(l)
print('is at postition', binarySearch(l, key) + 1)