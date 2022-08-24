from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cant_hear_listen = []
for _ in range(n+m):
    cant_hear_listen.append(input().rstrip())
count = Counter(cant_hear_listen)

res_num = 0
res_li = []
for i in count:
    if count[i] == 2:
       res_num += 1
       res_li.append(i)
print(res_num)
res_li.sort()
for i in res_li:
    print(i)


