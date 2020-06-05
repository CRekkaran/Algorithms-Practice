def solve(s, d):
	res = 0
	n = len(s)
	s = [x for x in s]
	i = 0
	while(i+d<=n):
		max1 = -1
		for j in range(d):
			if(s[i+j]=='1'):
				max1 = j
		if(max1==-1):
			s[i+d-1] = '1'
			i += d-1
			res += 1
		elif(max1>0):
			i += max1-1
		i += 1
	# print(''.join(s))
	return res


s = str(input())
d = int(input())
print(solve(s, d))
