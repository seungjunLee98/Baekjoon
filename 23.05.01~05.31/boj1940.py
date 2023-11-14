import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
armors = list(map(int, input().split()))
cnt = 0

armors.sort() # 정렬해서 보아도 무방하다.

for i in range(n//2+1):
    for j in range(n-1, i, -1):
        if armors[i]+armors[j]==m:
            cnt += 1

print(cnt)