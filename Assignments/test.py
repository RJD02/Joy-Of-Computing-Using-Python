import random

def brute(n):
    print("Brute: ", end = " ")
    #  n = int(input())
    if n % 2 == 1:
        print('invalid')
        return
    count = 0
    for i in range(2, n, 2):
        if n % i == 0:
            count += 1
            #  print(i)
            #  continue
        for j in range(0, n, 2):
            if i + j == n and i != j:
                count += 1
                #  print(i, j)
        #  print(count)
    print(count + 1)


def solve(n):
    print("solve: ", end = " ")
    #  n = int(input())
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
        #  print(n % i, i)
    print(count)
    return
#
#  n = 1
#  while True:
    #  s = solve(n)
    #  b = brute(n)
    #  if s != b:
        #  print("n = ", n, "solve = ", s, "brute = ", b)
        #  break
    #  else:
        #  print('ok')
    #  #  n = random.randint(0, 100)
    #  n += 1
n = int(input())
solve(n)
brute(n)
