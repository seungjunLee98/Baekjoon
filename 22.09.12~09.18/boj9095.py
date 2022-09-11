import sys
input = sys.stdin.readline

t = int(input().rstrip())
d = [0]* 11
d[1] = 1
d[2] = 2
d[3] = 4
for _ in range(t):
    n = int(input().rstrip())
    if d[n] != 0:
        print(d[n])
    else:
        for i in range(4, 11):
            d[i] = d[i - 1] + d[i - 2] + d[i - 3]
        print(d[n])
