from collections import deque
import sys
input = sys.stdin.readline

def bfs(tmp_graph, selected_wall, virus):
    tmp = [x[:] for x in tmp_graph]
    for x in selected_wall :
        tmp[x[0]][x[1]] = 1

    v = (1, 0, -1, 0)
    h = (0, 1, 0, -1)

    q = deque()
    for x in virus:
        q.append(x)

    res = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + v[k], j + h[k]
            if tmp[ni][nj] == 0:
                tmp[ni][nj] = 2
                q.append((ni, nj))
        res += 1
    return res



n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

tmp_graph = [[1]*(m+2)] + [[1]+x+[1] for x in graph] + [[1]*(m+2)]

empty = []
virus = []

for i in range(len(tmp_graph)):
    for j in range(len(tmp_graph[0])):
        if tmp_graph[i][j]==0:
            empty.append((i, j))
        elif tmp_graph[i][j]==2:
            virus.append((i, j))

res = n*m

for x in range(len(empty)):
    for y in range(x+1, len(empty)):
        for z in range(y+1, len(empty)):
            selectd_wall = [empty[x], empty[y], empty[z]]
            res = min(bfs(tmp_graph, selectd_wall, virus), res)

print(len(empty) + len(virus) - res - 3)

