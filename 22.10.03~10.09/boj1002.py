import sys
import math
input = sys.stdin.readline
# t는 테이스케이스의 개수
t = int(input().rstrip())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # d는 두 점 사이의 거리의 공식을 이용해서 구한다.
    d = math.sqrt((x1-x2)**2+(y1-y2)**2)

    # 두 원의 중심이 같은 좌표일 경우
    if d == 0:
        if r1 == r2: # 두 원의 반지름이 같을 경우
            result = -1 # 마린은 무한히 많다.
        else: # 두 원의 반지름이 다를 경우
            result = 0 # 마린은 존재할 수 없다.

    # 두 원의 중심이 다른 좌표일 경우
    else:
        if r1+r2 == d or abs(r1-r2) == d: # 두 원이 한 점에서 내접 or 외접할 경우
            result = 1
        elif abs(r1-r2) < d < r1+r2: # 두 원이 두 점에서 만나는 경우
            result = 2
        else: # 두 원이 만나지 못하는 경우
            result = 0
    print(result)


