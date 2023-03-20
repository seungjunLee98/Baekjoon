T = int(input())
ans = []
t_list = [300, 60, 10]
for i in t_list:
    ans.append(T // i)
    T %= i

if T == 0:
    for j in ans:
        print(j, end=' ')
else:
    print(-1)
