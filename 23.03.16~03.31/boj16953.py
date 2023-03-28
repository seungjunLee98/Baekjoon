# 가능한 연산은 두 가지
# A-> B
# 1. 곱하기 2
# 2. 문자열로 1을 맨 오른쪽에 추가시킨다 (append)
a, b = map(int, input().split())
cnt = 0
while a!=b:
    if a > b:
        print(-1)
        break
    elif (b-1)%10==0:
        b=(b-1)//10
        cnt+=1
    elif b%2==0:
        b//=2
        cnt+=1
    else:
        print(-1)
        break
if a==b:
    print(cnt+1)
