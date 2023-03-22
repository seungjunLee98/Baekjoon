import heapq
import sys
input = sys.stdin.readline

n = int(input())
card = []
ans, tmp = 0, 0

for _ in range(n):
    heapq.heappush(card,int(input()))


if len(card) == 1: # 비교횟수 이므로 card가 1장이라면 0회 비교다.
    print(0)
else:
    while len(card)>1:
        tmp = heapq.heappop(card) + heapq.heappop(card) # 누적 값을 할당해줄 tmp 변수
        ans += tmp
        heapq.heappush(card, tmp)
    print(ans)
