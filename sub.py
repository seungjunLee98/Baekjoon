N, K = map(int, input().split())
coin_list = []
count = 0
for _ in range(N):
    c = int(input())
    coin_list.append(c)

coin_list.reverse()

for coin in coin_list:
    count += K // coin
    K %= coin

print(count)