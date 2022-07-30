#내 풀이

#find 함수를 사용해서 인덱스 값으로 접근하기 위해 문자열을 준비한다.
x = "abcdefgh"
y = "12345678"

# 이동 거리를 int 값으로 리스트를 생성해뒀다
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2 ,-1]

#문자열로 입력 받는다.
pos = input()
count=0
#문자열을 찢어준다.
pos_col = pos[0]
pos_row = pos[1]


# 주어진 값의 인덱스 번호를 찾는다.
for i in x:
    for j in y:
        if i==pos_col and j==pos_row:
            pos_col_index_num = x.find(i)
            pos_row_index_num = y.find(j)

#인덱스 번호를 이용해 0보다 큰 값 8보다 작은 값을 카운팅 한다.
for k in range(len(dx)):
    if pos_col_index_num+dx[k]<8 and pos_col_index_num+dx[k]>=0 and pos_row_index_num+dy[k] >=0 and pos_row_index_num+dy[k]<8:
        count+=1

print(count)
















