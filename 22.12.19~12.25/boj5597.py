import sys
input = sys.stdin.readline

print_li = [] # 출력용 리스트(정렬해줘야 하기 때문에 만들었다)

# 출석번호 검증용 리스트
verify_list = [0 for _ in range(31)] # 출석번호는 1부터 시작

# 입력 받기
for _ in range(28):
    tmp = int(input())
    verify_list[tmp] = 1 # 방문처리

# 검증 하기
for i in range(1, 31):
    if verify_list[i] == 0: # 방문하지 않았다면
        print_li.append(i)

print_li.sort() #문제 조건에 따라 정렬해주기

# 출력해주기 한줄씩
for i in range(len(print_li)):
    print(print_li[i])