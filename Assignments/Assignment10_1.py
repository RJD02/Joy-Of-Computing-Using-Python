def solve():
    n = int(input())
    matrix = [[] for i in range(n)]
    l = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(n):
            matrix[i].append(l[count])
            count += 1
    #  print(matrix)
    d = {x:0 for x in range(n)}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                d[i] += 1
    #  print(d)
    for i in d.keys():
        if d[i] == 2:
            print('yes', i + 1)
            return
    print('no')
    return

solve()
