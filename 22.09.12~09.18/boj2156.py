import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = []
d = [0]*n
for _ in range(n):
    arr.append(int(input().rstrip()))

if n == 1:
    d[0] = arr[0]
    print(d[n-1])
elif n == 2:
    d[0] = arr[0]
    d[1] = arr[1] + d[0]
    print(d[n-1])
elif n == 3:
    d[0] = arr[0]
    d[1] = arr[1] + d[0]
    d[2] = max(d[1], d[0] + arr[2], arr[2] + arr[1])
    print(d[n-1])
else:
    d[0] = arr[0]
    d[1] = arr[1] + d[0]
    d[2] = max(d[1], d[0]+arr[2], arr[2]+arr[1])
    for i in range(3, n):
        d[i] = max(d[i-1], d[i-2]+arr[i], d[i-3]+arr[i-1]+arr[i])
    print(d[n-1])