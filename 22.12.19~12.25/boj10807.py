n = int(input()) # 파이썬은 동적할당으로 인해 안써도 무방하다.
li = list(map(int, input().split()))
v = int(input())
cnt = 0 # 카운팅해주기

for i in range(len(li)):
    if li[i]==v:
        cnt+=1

print(cnt)