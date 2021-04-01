def solve():
    n = int(input())
    if n % 2 == 1:
        print('invalid')
        return
    ways = [1 for _ in range(n // 2)]
    for i in range(1, n // 2):
        ways[i] = 2 * ways[i - 1]
    print(ways[n // 2 - 1])
    return

solve()
