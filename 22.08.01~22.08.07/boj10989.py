import sys
n = int(sys.stdin.readline())
b = [0]*10001
for i in range(n):
    b[int(sys.stdin.readline())]+=1
for j in range(10001):
    if b[j] != 0:
        for k in range(b[j]):
            print(j)

