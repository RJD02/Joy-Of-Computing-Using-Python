def check(n):
    if n % 10 != 4:
        return True
    else:
        return False

str = input()
# li = []
# j = 0
for i in str:
    if i == " ":
        continue
    elif check(int(i)):
        print(int(i), end=" ")
    else:
        continue
