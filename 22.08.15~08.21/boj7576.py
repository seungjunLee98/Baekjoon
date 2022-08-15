from collections import deque

m, n = map(int, input().split())

graph = []
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j]) # 여기는 출발 위치를 찾는중

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0) # 더 이상 찾을 필요가 없기 때문에 깔끔한 종료
    result = max(result, max(i))

print(result-1) # 날짜 수를 세는 것이기 때문에 -1을 해준다.






