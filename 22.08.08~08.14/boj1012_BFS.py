import sys
from collections import deque

def bfs(x, y):
    q = deque([(x,y)])
    while q: # q가 빌 때까지 반복
        x, y = q.popleft()

        for i in range(4): # 상, 하, 좌, 우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 2
    return 1

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)
    print(cnt)