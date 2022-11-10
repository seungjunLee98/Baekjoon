import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        c = a[i][j] + b[i][j]
        if m!=(j+1):
            print(c, end=' ')
        else:
            print(c)



