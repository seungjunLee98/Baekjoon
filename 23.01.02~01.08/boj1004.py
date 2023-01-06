import math

t = int(input())

for _ in range(t): # 테스트 케이스
    x1, y1, x2, y2 = map(int, input().split()) # 좌표. 출발점 (x1, y1)과 도착점 (x2, y2)
    n = int(input())
    ans = 0
    for _ in range(n): # 행성의 개수
        cx, cy, r = map(int, input().split()) # 행성계의 중점과 반지름 (cx, cy, r)
        if math.sqrt((x1-cx)**2 + (y1 - cy)**2) < r and math.sqrt((x2-cx)**2 + (y2 - cy)**2) < r: # 출발점 도착점이 원 안에 있을 때
            ans += 0
        elif math.sqrt((x1-cx)**2 + (y1 - cy)**2) < r: # 두 점 사이의 거리가 r보다 작을 때 반드시 한 번 지나간다.
            ans += 1
        elif math.sqrt((x2-cx)**2 + (y2 - cy)**2) < r:
            ans += 1
    print(ans)