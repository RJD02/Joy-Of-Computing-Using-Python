def solve():
    count_snakes = 0
    count_ladders = 0
    line = input().split(",")
    c = []
    for i in line:
        c.append(i.split(":"))
    for i in c:
        i[0] = int(i[0])
        i[1] = int(i[1])
    for i in c:
        if i[0] < i[1]:
            count_ladders += 1
        elif i[0] > i[1]:
            count_snakes += 1
    print(count_snakes,count_ladders)

solve()
