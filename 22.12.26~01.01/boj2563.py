import sys
input = sys.stdin.readline

n = int(input()) # black paper

graph = [[0]*100 for _ in range(100)] # white paper

result = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if graph[i][j] == 0:
                graph[i][j] = 1
                result += 1
print(result)