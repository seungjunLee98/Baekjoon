# 입력에 따른 시간을 줄이기 위해 사용
import sys
input = sys.stdin.readline


graph = []
max_value = 0

r = 1
c = 1

for _ in range(9):
    graph.append(list(map(int, input().split())))


for i in range(9):
    if max_value < max(graph[i]):
        max_value = max(graph[i])
        r, c = i+1, graph[i].index(max_value)+1

print(max_value)
print(r, c)

