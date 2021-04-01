def solve():
    row, col = input().split(" ")
    row, col = int(row), int(col)
    for i in range(row):
        col_val = input().split(" ")
        col_val = [int(x) for x in col_val]
        for y in col_val:
            if y != 0 and y != 1:
                print('No')
                return
    print('Yes')
    return

def solve():
    row, col = map(int, input().split(" "))
    mat = [list(map(int, input().split())) for i in range(m)]
    for i in range(row):
        for j in range(col):
            if mat[i][j] != 0 and mat[i][j] != 1:
                print('No')
                break
    else:
        print('Yes')
    return

solve()
