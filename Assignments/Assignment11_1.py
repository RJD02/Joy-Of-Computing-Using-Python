def solve(n):
    n = int(input())
    if n == 0:
        print(1)
        return
    if n % 2 == 1:
        print('invalid')
        return
    count = 0
    for i in range(2, n + 1, 2):
        if n % i == 0:
            count += 1
        elif (n % i) % 2 == 0:
            count += 2
    print(count)
    return

solve(n)
