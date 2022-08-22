import sys
input = sys.stdin.readline

li = []
for _ in range(9):
    li.append(int(input()))

li = sorted(li)
other = sum(li)-100
one, two = 0, 0
for i in range(8):
    for j in range(i+1, 9):
        if li[i]+li[j] == other:
            one, two = li[i], li[j]

li.remove(one)
li.remove(two)
for k in li:
    print(k)

