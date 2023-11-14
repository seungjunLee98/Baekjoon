n = int(input())
t_list = [] # day
p_list = [] # money
for _ in range(n):
    a, b = map(int, input().split())
    t_list.append(a)
    p_list.append(b)

d = [0 for _ in range(n + 1)]

for i in range(n):
    for j in range(i+t_list[i], n+1):
        if d[j] < d[i] + p_list[i]:
            d[j] = d[i] + p_list[i]

print(d[-1])