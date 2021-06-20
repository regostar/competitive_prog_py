t = int(input())


def shop(n, cost):
    sorted_costs = sorted(cost, reverse=True)
    cost_to_be_paid = 0
    i=0
    if len(cost) <= 2:
        cost_to_be_paid = sum(cost)
        return cost_to_be_paid
    while i<len(cost):
        cost_to_be_paid += sorted_costs[i] + sorted_costs[i+1]
        i += 4 
    return cost_to_be_paid

for _ in range(t):
    n = int(input())
    cost = list(map(int,input().split()))
    shop(n, cost)

