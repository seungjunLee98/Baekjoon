def hanoi(n, start, end, tmp):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n-1, start, tmp, end)
        print(start, end)
        hanoi(n-1, tmp, end, start)

n = int(input())
sum = 1
for i in range(n-1):
    sum = sum*2 + 1

print(sum)

hanoi(n,1,3,2)

