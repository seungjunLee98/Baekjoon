s = input() # 입력은 문자열로 받아준다
li = [] # 문자열은 숫자로 변환하여 리스트에 담아줄거다.
verify_num = 0 # 합이 3의 배수인지 확인하기 위해 준비한다.
if '0' in s:
    for i in range(len(s)):
        li.append(int(s[i]))
    li.sort(reverse=True) # 가장 큰 30의 배수가 필요하기 때문에 존재
    for j in range(len(li)-1):
        verify_num += li[j]
    if verify_num % 3 == 0: # 3의 배수 규칙
        for k in range(len(li)):
            print(li[k], end='')
    else:
        print(-1)
else:
    print(-1)