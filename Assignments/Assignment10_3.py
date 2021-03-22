def solve():
    n = int(input())
    matrix = [[] for i in range(n)]
    l = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(n):
            matrix[i].append(l[count])
            count += 1
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif matrix[i][j] != 1:
                print('no')
                return
    print('yes')
    #  print(matrix)
    return

solve()
