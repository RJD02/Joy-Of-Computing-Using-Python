def solve():
    l1 = input().split(" ")
    l2 = input().split(" ")
    l1 = [int(x) for x in l1]
    l2 = [int(x) for x in l2]
    count_l2 = 0
    for i in l1:
        if i != l2[count_l2]:
            print('No')
            break
        count_l2 += 1
    else:
        print('Yes')


solve()
