import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))

d = [0]*(k+1)

d[0] = 1

for i in arr:
    for j in range(i, k+1):
        d[j] += d[j-i]

print(d[k])