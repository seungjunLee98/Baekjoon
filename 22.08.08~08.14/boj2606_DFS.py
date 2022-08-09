# DFS 재귀적으로 푸는법

# 1. 첫째줄에 컴퓨터의 수가 주어진다.
n = int(input())

# 1. 네트워크 상 연결되어 있는 컴퓨터의 수
connected = int(input())

# 2. 인접리스트 그래프의 형태를 그려주고 입력받는다.
graph = [[] for _ in range(n+1)] # n+1 하는 이유는 인덱스 번호를 활용하기 위해서다.
# 0번째 컴퓨터는 문제 조건에 따라 쓰이지 않음.

for _ in range(connected):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

def dfs(graph, v, visited):
    visited[v] = 1 # 방문 처리
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True
dfs(graph, 1, visited)
print(sum(visited)-1)
