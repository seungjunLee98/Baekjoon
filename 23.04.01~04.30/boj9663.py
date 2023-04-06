import sys
input = sys.stdin.readline
n = int(input())
ans = 0
board = [0]*n # 인덱스를 행으로 값을 열로 사용한다.
def is_promising(x):
    for i in range(x):
        if board[x]==board[i] or abs(board[x]-board[i]) == abs(x-i):
            return False
    return True

def dfs(x):
    global ans
    if x==n:
        ans+=1
    else:
        for i in range(n):
            board[x] = i
            if is_promising(x):
                dfs(x+1)

dfs(0)
print(ans)