import sys
from collections import deque
read = sys.stdin.readline

n, m, v = map(int, read().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m): # 그래프 생성
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)): # 그래프 정렬
    graph[i].sort()

def dfs(start):
    print(start, end=' ')
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

dfs(v)
visited = [0] * (n+1) # visited 리스트 초기화
print()
bfs(v)

