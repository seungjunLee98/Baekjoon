from collections import deque
import sys
import copy
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx, ny))
    global result
    count = 0
    for k in range(n):
        for l in range(m):
            if tmp_graph[k][l] == 0:
                count += 1

    result = max(result, count)

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
result = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
make_wall(0)
print(result)





