n, m = map(int, input().split())
chess_pan = []
count_list = []
for _ in range(n):
    chess_pan.append(input())

for j in range(n-7):
    for k in range(m-7): #start지점 구하기
        count_B = 0
        count_W = 0
        for l in range(j,j+8):
            for n in range(k, k+8):
                if (l+n) % 2 == 0: # 현재 행의 번호 l, 현재 열의 번호 n의 합이 짝수이면 시작점의 색깔과 같아야 한다.
                    if chess_pan[l][n] != 'W': # 'W' 로 시작한 경우 바꿔야 할 'B' 의 갯수를 카운트
                        count_B += 1
                    if chess_pan[l][n] != 'B': # 'B' 로 시작한 경우 바꿔야 할 'W' 의 갯수를 카운트
                        count_W += 1
                else: # 홀수이면 시작점의 색깔과 다른 색이어야 한다.
                    if chess_pan[l][n] != 'B': # 'B' 로 시작한 경우 바꿔야 할 'B' 의 갯수를 카운트
                        count_B += 1
                    if chess_pan[l][n] != 'W': # 'W' 로 시작한 경우 바꿔야 할 'W' 의 갯수를 카운트
                        count_W += 1
        count_list.append(count_W)
        count_list.append(count_B) # 'W'로 시작할 경우와 'B'로 시작할 경우 바뀐 체스판의 수 중 작은 수를 count 리스트에 더해준다.

print(min(count_list)) # 모든 경우의 수를 다 체크한 후, count 중 제일 작은 수를 출력하고 프로그램을 종료한다.