import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 1
    res = []
    for _ in range(n):
        grade, rank = map(int, input().split())
        res.append((grade, rank))
    res.sort(key=lambda x:x[0])
    tmp = res[0][1]
    for i in range(len(res)-1):
        if tmp > res[i+1][1]:
            cnt += 1
            tmp = res[i+1][1]
    print(cnt)




