from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
MAX = 100000
visited = [0] * (MAX+1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for i in (x-1, x+1, 2*x):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
bfs()



