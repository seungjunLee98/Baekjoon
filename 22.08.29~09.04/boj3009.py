from collections import Counter

li = []
for _ in range(3):
    li.append(list(map(int, input().split())))

x_li = Counter([li[i][0] for i in range(3)])
y_li = Counter([li[j][1] for j in range(3)])

print(x_li.most_common(2)[1][0], y_li.most_common(2)[1][0])
