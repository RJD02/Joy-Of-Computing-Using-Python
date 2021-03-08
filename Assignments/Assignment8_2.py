def solve():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input().split(" "))
    l = [[int(x) for x in l[i]] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if l[i][j] != l[j][i]:
                print('No')
                return
    print('Yes')
    return

solve()
