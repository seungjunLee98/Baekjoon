n = int(input())
graph = []
for _ in range(n):
    graph.append(tuple(map(int, input().split())))

result = sorted(graph, key= lambda x : (x[0], x[1]))

for i in result:
    print(f"{i[0]} {i[1]}")
