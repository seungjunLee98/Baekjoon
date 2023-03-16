n = int(input()) # numbers of city
roads = list(map(int, input().split())) # length of roads
costs = list(map(int, input().split())) # the price per liter at a gas station

result = 0
m = costs[0]
for i in range(n-1):
    if costs[i] < m:
        m = costs[i]
    result += m*roads[i]
print(result)
