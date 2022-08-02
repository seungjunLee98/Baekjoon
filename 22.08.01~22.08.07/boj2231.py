def decomposition_sum(k):
    sum_k = k
    str_k = str(k)
    for m in range(len(str_k)):
        sum_k += int(str_k[m])
    return sum_k


n = int(input())

n_generator = []

for i in range(1, n+1):
    if decomposition_sum(i)==n:
        n_generator.append(i)



if len(n_generator) == 0:
    print(0)
else:
    print(min(n_generator))