def solve():
    n = int(input())
    ramesh = input().split()
    suresh = input().split()
    count = 0
    for i in range(n):
        if ramesh[i] != suresh[i] and ramesh[i] != '.':
            count += 1
    print(count)
    return

solve()
