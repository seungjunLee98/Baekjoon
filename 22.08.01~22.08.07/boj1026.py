N = int(input())
A = list(map(int, input().split())) # A 배열 생성
B = list(map(int, input().split())) # B 배열 생성

B_tmp = B

A.sort()
B_tmp.sort()
B_tmp.reverse()

S = 0
for i in range(N):
    S+= A[i]*B_tmp[i]
print(S)

