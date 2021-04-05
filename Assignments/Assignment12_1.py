def solve():
    p1 = list(map(float, input().split()))
    p2 = list(map(float, input().split()))
    p3 = list(map(float, input().split()))
    d1 = p1[0] * (p2[1] * p3[2] - p2[2] * p3[1])
    d2 = p1[1] * (p2[0] * p3[2] - p2[2] * p3[0])
    d3 = p1[2] * (p2[0] * p3[1] - p2[1] * p3[0])
    res = (d1 - d2 + d3)
    print(abs(res))
    return

solve()
