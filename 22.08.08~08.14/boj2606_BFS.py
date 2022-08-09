# BFS로 푸는법 (이론상 더 효율적이다.)
# 1. 첫째줄에 컴퓨터의 수가 주어진다.
n = int(input())

# 1. 네트워크 상 연결되어 있는 컴퓨터의 수
connected = int(input())

# 2. 인접리스트 그래프의 형태를 그려주고 입력받는다.
graph = [[] for _ in range(n+1)]

for _ in range(connected):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [0] * (n+1)

from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])

    while queue:
        now = queue.popleft()
        # 현재 컴퓨터를 방문 처리
        visited[now] = 1

        # 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 Queue에 삽입하고 방문처리
        for i in graph[now]:
            if visited[i] == 0:
                queue.append(i)

bfs(graph, 1, visited)

print(sum(visited)-1)