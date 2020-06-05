import math
import os
import random
import re
import sys

class Graph: 
      
    def __init__(self):
        self.res = '0 '

    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        # from the dist array,pick one which 
        # has min value and is till in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
  
    # Function to print shortest path 
    # from source to j 
    # using parent array 
    def printPath(self, parent, j): 
          
        #Base Case : If j is source 
        if parent[j] == -1 :  
            # print(j, end=" ")
            return
        self.printPath(parent , parent[j]) 
        # print(j, end=" ")
        self.res += str(j) + ' '

    def printSolution(self, dist, parent): 
        src = 0
        return self.printPath(parent, len(dist)-1)

    def dijkstra(self, graph, src): 
  
        row = len(graph) 
        col = len(graph[0]) 

        dist = [float("Inf")] * row 
  
        parent = [-1] * row 
  
        dist[src] = 0
      
        queue = [] 
        for i in range(row): 
            queue.append(i) 
              
        while queue: 
  
            u = self.minDistance(dist,queue)  
  
            queue.remove(u) 
  
            for i in range(col): 
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
  
  
        return self.printSolution(dist,parent) 

def getMinEffort(arr):
    # Write your code here
    n = len(arr)
    m = len(arr[0])
    
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
        temp = [0 for i in range(cnt)]
        adjMat.append(temp)
    # print(adjMat)

    for i in range(n):
        for j in range(m):
            if(j+1<m):
                adjMat[id[(i, j)]][id[(i, j+1)]] = abs(arr[i][j]-arr[i][j+1])
            if(j-1>=0):
                adjMat[id[(i, j)]][id[(i, j-1)]] = abs(arr[i][j]-arr[i][j-1])
            if(i-1>=0):
                adjMat[id[(i, j)]][id[(i-1, j)]] = abs(arr[i][j]-arr[i-1][j])
            if(i+1<n):
                adjMat[id[(i, j)]][id[(i+1, j)]] = abs(arr[i][j]-arr[i+1][j])

    # print(adjMat)

    g = Graph()
    g.dijkstra(adjMat, 0)
    final = [int(x) for x in g.res.split(' ')[:-1]]
    
    maxdiff = -1
    for i in range(1, len(final)):
        if(maxdiff<abs(arr[rev_id[final[i]][0]][rev_id[final[i]][1]] - arr[rev_id[final[i-1]][0]][rev_id[final[i-1]][1]])):
            maxdiff = abs(arr[rev_id[final[i]][0]][rev_id[final[i]][1]] - arr[rev_id[final[i-1]][0]][rev_id[final[i-1]][1]])
    return maxdiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    answer = getMinEffort(arr)

    fptr.write(str(answer) + '\n')

    fptr.close()
