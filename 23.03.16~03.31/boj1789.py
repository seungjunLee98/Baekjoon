s = int(input()) # 초기값
n = 0 # 누적 값
i = 1 # 자연수니까 1부터 더해가겠다.
cnt = 0 # 더한 값 카운팅
while True:
    if n+i < s:
        n += i
        cnt += 1
        i+=1
    elif n+i == s:
        n += i
        cnt += 1
        break
    elif n+i > s:
        n = s-i
        cnt -= 1
print(cnt)