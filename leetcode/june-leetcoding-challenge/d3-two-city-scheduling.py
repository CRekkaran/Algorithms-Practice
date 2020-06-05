def twoCitySchedCost(costs):
    total_a = 0
    total_b = 0
    n = len(costs)
    res = 0
    i = 0

    while(i<n and total_a+total_b!=n):
        ind = costs[i].index(min(costs[i]))
        
    return res

# lst = [[10,20],[30,200],[400,50],[30,20]]
lst = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(twoCitySchedCost(lst))