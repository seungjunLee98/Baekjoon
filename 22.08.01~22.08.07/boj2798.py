n, m = map(int, input().split())
card_list = list(map(int, input().split()))

sum_list = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card_list[i]+card_list[j]+card_list[k] <= m:
                sum_list.append(card_list[i]+card_list[j]+card_list[k])

sum_list.sort()
print(sum_list[-1])


