def solve():
    line_input = input().split(",")
    pair = [i.split(":") for i in line_input]
    for i in range(len(pair)):
        pair[i][1] = pair[i][1].strip()
    for i in range(len(pair)):
        for j in range(2):
            pair[i][j] = int(pair[i][j])
    dice = input().split(", ")
    for i in range(len(dice), 2):
        dice[i] = dice[i].strip()
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
