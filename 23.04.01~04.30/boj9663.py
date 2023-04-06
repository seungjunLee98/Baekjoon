import sys
input = sys.stdin.readline
n = int(input())
ans = 0
board = [0]*n # 인덱스를 행으로 값을 열로 사용한다. 인덱스가 행 board[n]값이 열
def is_promising(x):
    for i in range(x):
        if board[x]==board[i] or abs(board[x]-board[i]) == x-i: # 열이 같거나 대각선이 같으면 false
            return False
    return True

def dfs(x):
    global ans
    if x==n:
        ans+=1
    else:
        # 각 행에 퀸 놓기
        for i in range(n): # i는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
            board[x] = i
            if is_promising(x): # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
                dfs(x+1)

dfs(0)
print(ans)