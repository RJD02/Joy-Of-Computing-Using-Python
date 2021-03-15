def solve():
	line = input()
	res = ""
	for i in line:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
			continue
		res += i
	print(res)

solve()