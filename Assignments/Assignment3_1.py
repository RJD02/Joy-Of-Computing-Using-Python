l = list(input().split(" "))
for i in range(len(l)):
    l[i] = int(l[i])
    if abs(l[i]) % 10 != 4:
        print(l[i], end=" ")
