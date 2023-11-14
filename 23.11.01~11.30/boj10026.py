import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
graph = []
for i in range(n):
    graph.append(list(map(str, input().rstrip())))

visited = [[False]*n for _ in range(n)]
two_cnt = 0
thr_cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    visited[x][y] = True
    current_color = graph[x][y]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0<=nx<n) and (0<=ny<n):
            if visited[nx][ny] == False:
                if graph[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            thr_cnt += 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1
print(thr_cnt, two_cnt)
'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''