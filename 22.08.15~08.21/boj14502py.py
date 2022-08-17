import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
virus_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus_list.append([i,j])

def make_wall(start, count):
    global result
    if count == 3:
        tmp_graph = copy.deepcopy(graph)
        for num in range(len(virus_list)):
            x, y = virus_list[num]
            spread_virus(x, y, tmp_graph)
        safe_counts = sum(i.count(0) for i in tmp_graph)
        result = max(result, safe_counts)
        return True
    else:
        for i in range(start, n*m):
            x = i//m
            y = i%m
            if graph[x][y] == 0:
                graph[x][y] = 1
                make_wall(i, count+1)
                graph[x][y] = 0

def spread_virus(x, y, tmp_graph):
    if tmp_graph[x][y] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    spread_virus(nx, ny, tmp_graph)

make_wall(0, 0)
print(result)
