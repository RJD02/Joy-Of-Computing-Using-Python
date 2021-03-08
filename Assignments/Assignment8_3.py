def solve():
    n = int(input())
    count = 1
    for i in range(n):
        for j in range(n):
            if j == n - 1:
                print(count, end = "")
            else:
                print(count, end = " ")
            count += 1
        print()
    return

solve()
