import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

# 시작 시간을 기준으로 정렬
li = sorted(li, key=lambda a: a[0])
# 끝나는 시간을 기준으로 정렬
li = sorted(li, key=lambda a: a[1])


last = 0
cnt = 0

# 정렬을 끝낸 상태
for i, j in li:
    if i >= last:
        cnt += 1
        last = j
print(cnt)



