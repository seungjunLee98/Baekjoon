import sys
sys.setrecursionlimit(10000) # 런타임에러 방지용

t = int(sys.stdin.readline())

for _ in range(t): # 테스트 케이스
    m, n, k = map(int, sys.stdin.readline().split()) # m,n,k 입력
    graph = [[0]*m for _ in range(n)] # 가로m, 세로n의 형태를 띈 그래프 생성
    for _ in range(k): # 배추의 위치정보 기록
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    def dfs(x, y):
        # 주어진 범위를 벗어난 경우에는 즉시 종료
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        # 현재 노드를 아직 방문하지 않았다면
        if graph[y][x] == 1:
            graph[y][x] = 0
            dfs(x, y-1) # 상
            dfs(x+1, y) # 우
            dfs(x, y+1) # 하
            dfs(x-1, y) # 좌
            return True
        # 0 이면 False
        return False
    # 필요한 배추흰지렁이의 수
    cnt = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 탐색
            if dfs(j, i) == True:
                cnt += 1
    print(cnt)


