def solve():
	n = int(input())

	temp1 = input()
	temp2 = input()

	b = [int(x) for x in temp1.split(' ')]
	g = [int(x) for x in temp2.split(' ')]

	res = []

	pos1 = 0
	pos2 = 0
	if(b[pos1]<g[pos2]):
		res.append('b')
		pos1 += 1
	else:
		res.append('g')
		pos2 += 1
	while(pos1<n and pos2<n):
		if(res[-1]=='b'):
			if(g[pos2]<=b[pos1]):
				pos2 += 1
				res.append('g')
			else:
				return 'NO'
		else:
			if(b[pos1]<=g[pos2]):
				pos1 += 1
				res.append('b')
			else:
				return 'NO'
	return 'YES'

for _ in range(int(input())):
	print(solve())