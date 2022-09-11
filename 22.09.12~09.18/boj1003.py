import sys
input = sys.stdin.readline

t = int(input().rstrip())
d = [0] * 41
cnt_0 = [0] * 41
cnt_1 = [0] * 41


def fib(x):
    if x == 0:
        cnt_0[0] = 1
        return 0
    elif x == 1:
        cnt_1[1] = 1
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    cnt_0[x] = cnt_0[x-1] + cnt_0[x-2]
    cnt_1[x] = cnt_1[x-1] + cnt_1[x-2]
    return d[x]

for i in range(t):
    n = int(input().rstrip())
    fib(n)
    print(cnt_0[n], cnt_1[n])


