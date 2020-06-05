import numpy as np
from collections import deque

def solve(n, m):
	arr = []
	for j in range(n):
		temp = [int(x) for x in input().split(' ')[:-1]]
		arr.append(temp)	
	
	cnt = 0
	id = {}
	rev_id = {}
	for i in range(n):
		for j in range(m):
			id[(i,j)] = cnt
			rev_id[cnt] = (i,j)
			cnt += 1
	
	adjMat = []
	for i in range(cnt):
		temp = [-1 for i in range(4)]
		adjMat.append(temp)

	for i in range(n):
		for j in range(m):
			if(j+1<m):
				adjMat[id[(i, j)]][1] = abs(arr[i][j]-arr[i][j+1])
			if(j-1>=0):
				adjMat[id[(i, j)]][3] = abs(arr[i][j]-arr[i][j-1])
			if(i-1>=0):
				adjMat[id[(i, j)]][0] = abs(arr[i][j]-arr[i-1][j])
			if(i+1<n):
				adjMat[id[(i, j)]][2] = abs(arr[i][j]-arr[i+1][j])
	
	# print(adjMat)

	q = deque()
	q.append(id[(0, 0)])

	B = [10**6 for i in range(cnt)]
	B[0] = 0
	visited = {}
	for i in range(cnt):
		visited[i] = False

	while(len(q)!=0):
		# print(q)
		
		temp = q.popleft()
		
		if(visited[temp]==True):
			continue

		lst = adjMat[temp]

		for i in range(len(lst)):
			if(lst[i]==-1):
				continue
			else:
				x, y = rev_id[temp]
				if i==0:
					if(visited[id[x-1, y]]):
						continue
					q.append(id[x-1, y])
					designated = B[id[(x-1,y)]]
					new_designated = B[id[(x,y)]]+lst[i]
					if(new_designated<designated):
						B[id[(x-1,y)]] = B[id[(x,y)]]+lst[i]
				elif i==1:
					if(visited[id[x, y+1]]):
						continue
					q.append(id[x, y+1])
					designated = B[id[(x,y+1)]]
					new_designated = B[id[(x,y)]]+lst[i]
					if(new_designated<designated):
						B[id[(x,y+1)]] = B[id[(x,y)]]+lst[i]
				elif i==2:
					if(visited[id[x+1, y]]):
						continue
					q.append(id[x+1, y])
					designated = B[id[(x+1,y)]]
					new_designated = B[id[(x,y)]]+lst[i]
					if(new_designated<designated):
						B[id[(x+1,y)]] = B[id[(x,y)]]+lst[i]
				elif i==3:
					if(visited[id[x, y-1]]):
						continue
					q.append(id[x, y-1])
					designated = B[id[(x,y-1)]]
					new_designated = B[id[(x,y)]]+lst[i]
					if(new_designated<designated):
						B[id[(x,y-1)]] = B[id[(x,y)]]+lst[i]
		visited[temp] = True
	
	print(B)

	# B = B[::-1]

	# pos1, pos2 = n-1, m-1
	# while(pos1!=0 or pos2!=0):
	# 	cost = B.popleft()
	# 	for i in range(4):
	# 		if(adjMat[id[pos1,pos2]][i]!=-1):
	# 			if(i==0 and B[id[arr[pos1-1][pos2]]] + adjMat[id[pos1,pos2]][2]==cost)

	path = [[]]

	a = cnt-1
	cntr = 0
	while(a!=0):
		
		if(cntr==n+m):
			break
		cntr += 1

		path[0].append(a)
		lst = adjMat[a]
		possible_ways = [10**6]*4
		for i in range(4):
			if(lst[i]==-1):
				continue
			X,Y = rev_id[a]
			if(i==0 and abs(B[id[X-1, Y]]-B[a]) == abs(arr[X-1][Y] - arr[X][Y]) and B[id[X-1, Y]]-B[id[(X, Y)]]<=0):
				# a -= m
				possible_ways[0] = abs(B[id[X-1, Y]]-B[a])
			if(i==1 and abs(B[id[X, Y+1]]-B[id[(X, Y)]]) == abs(arr[X][Y+1] - arr[X][Y]) and (B[id[X, Y+1]]-B[id[(X, Y)]])<=0):
				# a += 1
				possible_ways[1] = abs(B[id[X, Y+1]]-B[a])
			if(i==2 and abs(B[id[X+1, Y]]-B[id[(X, Y)]]) == abs(arr[X+1][Y] - arr[X][Y]) and B[id[X+1, Y]]-B[id[(X, Y)]]<=0):
				# a += m
				possible_ways[2] = abs(B[id[X+1, Y]]-B[a])
			if(i==3 and abs(B[id[X, Y-1]]-B[id[(X, Y)]]) == abs(arr[X][Y-1] - arr[X][Y]) and B[id[X, Y-1]]<=B[id[(X, Y)]]):
				# a -=1
				possible_ways[3] = abs(B[id[X, Y-1]]-B[a])
		index = possible_ways.index(min(possible_ways))
		print(possible_ways)
		if(index==0):
			a -= m
		elif(index==1):
			a += 1
		elif(index==2):
			a += m
		else:
			a -= 1
	path[0].append(a)
	xsx = []
	for i in range(len(path[0])-1):
		tt = arr[rev_id[path[0][i]][0] ][ rev_id[path[0][i]][1] ] - arr[rev_id[path[0][i+1]][0] ][ rev_id[path[0][i+1]][1] ]
		xsx.append(abs(tt))
	print(path)
	return max(xsx)

temp = [int(p) for p in input().split(' ')]
print(solve(temp[0], temp[1]))