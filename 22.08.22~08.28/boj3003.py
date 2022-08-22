# 원래 체스 피스 수
c = [1, 1, 2, 2, 2, 8]
# 동혁이가 찾은 피스 수
s = list(map(int, input().split()))

result = []
for i in range(len(c)):
    result.append(c[i]-s[i])

for j in result:
    print(j, end=" ")

