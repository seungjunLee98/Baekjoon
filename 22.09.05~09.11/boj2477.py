k = int(input().rstrip())
diretion = []
li = []
for _ in range(6):
    a, b = map(int, input().split())
    diretion.append(a)
    li.append(b)
odd_li = li[0::2]
even_li = li[1::2]

A = max(odd_li)
B = max(even_li)


li += li
diretion += diretion
for i in range(12):
    if diretion[i] == diretion[i+2]:
        if diretion[i+1] == diretion[i+3]:
            C = li[i+1]
            D = li[i+2]
            print((A * B - C * D) * k)
            exit(0)