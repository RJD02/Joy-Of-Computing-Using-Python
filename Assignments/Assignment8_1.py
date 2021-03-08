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

solve()
