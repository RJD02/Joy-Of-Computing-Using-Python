def solve():
    n = int(input())
    count = 0
    print((n * n + n + 4) // 2)
   #   for i in range(2 ** n):
        #  # convert to binary
        #  # check if there are any 2 adjacent
        #  curr = -1
        #  flag = True
        #  l = list(bin(i)[2:])
        #  while len(l) != n:
            #  l.append('0')
        #  #  l = l[::-1]
        #  print(l)
        #  for j in list(bin(i)[2:]):
            #  if curr == 0 and j == 0:
                #  flag = False
            #  curr = j
        #  if flag:
            #  count += 1
   #   print(count)
    return

solve()
