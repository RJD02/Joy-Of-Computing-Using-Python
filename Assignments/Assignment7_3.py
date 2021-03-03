def solve():
    line_input = input().split(",")
    pair = [i.split(":  ") for i in line_input]
    pair = [[int(i[0]), int(i[1])] for i in pair]
    dice = input().split(", ")
    dice = [int(x) for x in dice]
    count = 0
    for i in dice:
        count += i
        for i in pair:
            if i[0] == count:
                count = i[1]
        if count >= 100:
            print('Yes')
            break
    else:
        print('No')

solve()
