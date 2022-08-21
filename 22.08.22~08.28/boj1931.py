import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

li = sorted(li, key=lambda a: a[0])
li = sorted(li, key=lambda a: a[1])

last = 0
cnt = 0

for i, j in li:
    if i >= last:
        cnt += 1
        last = j
print(cnt)



