
n = input()

tmp = ""
li = []
cnt = 0

# 문자열 자르는 과정 {숫자(int)와 부호(str)를 나눈다.}
# - 부호 뒤에 오는 + 부호는 전부 -로 교체한다.
for i in range(len(n)):
    if n[i] != '-' and n[i] != '+':
        tmp += n[i]
    elif n[i] == '-':
        li.append(int(tmp))
        li.append(n[i])
        tmp = ""
        cnt = 1
    elif n[i] == '+':
        li.append(int(tmp))
        if cnt == 1:
            li.append('-')
        else:
            li.append(n[i])
        tmp = ""
li.append(int(tmp))
# ex) input : 55-50+40
#     li : [55, '-', 50, '-', 40]

# 리스트에 홀수번째는 전부 부호이므로
# 부호에 따라 result에 값을 담는다.
result = li[0]
for i in range(1,len(li), 2):
    if li[i] == '-':
        result -= li[i+1]
    elif li[i] == '+':
        result += li[i+1]
print(result)
