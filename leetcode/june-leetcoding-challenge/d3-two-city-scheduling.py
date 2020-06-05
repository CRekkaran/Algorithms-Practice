# Problem statement
# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Solution
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    refund = []
    N = len(costs)//2
    minCost = 0
    for A, B in costs:
        refund.append(B - A)
        minCost += A
    refund.sort()
    for i in range(N):
        minCost += refund[i]
    return minCost

# lst = [[10,20],[30,200],[400,50],[30,20]]
lst = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(twoCitySchedCost(lst))
