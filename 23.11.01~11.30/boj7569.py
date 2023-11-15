from collections import deque
import sys
input = sys.stdin.readline

# m은 가로, n은 세로, h는 높이
m, n, h = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

result = 0

# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0 or nz >= h or nz < 0:
                continue
            if matrix[nz][ny][nx] == 0 and visited[nz][ny][nx] == False:
                queue.append((nx,ny,nz))
                matrix[nz][ny][nx] = matrix[z][y][x] + 1
                visited[nz][ny][nx] = True

# 모든 토마토가 익어있는 경우
check = 0
for a in matrix:
    for b in a:
        for c in b:
            if c==0:
                check += 1
if check == 0:
    print(0)
    exit(0)


# 익은 토마토 위치를 append!
for a in range(h):
    for b in range(n):
        for c in range(m):
            if matrix[a][b][c] == 1 and visited[a][b][c] == False:
                queue.append((c,b,a))
                visited[a][b][c] = True

bfs()

# 모든 토마토가 익지 못하는 경우
for a in matrix:
    for b in a:
        for c in b:
            if c==0:
                print(-1)
                exit(0)


# 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력

for a in matrix:
    for b in a:
        result = max(max(b), result)
print(result-1)







