def solve():
	l = input().split(" ")
	l = [int(x) for x in l]
	k = int(input())
	res = []
	for i in l:
		if i not in res:
			res.append(i)
	d = {i:0 for i in res}
	# print(d)
	for i in l:
		d[i] += 1
	for i in d.keys():
		if d[i] == k:
			print(i)
	return

solve()