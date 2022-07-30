# 내 풀이

# N = int(input())
# plan_list = list(map(str, input().split()))
# x, y = 1, 1
#
# for plan in plan_list:
#     if plan=='U':
#         if x==1:
#             continue
#         else:
#             x-=1
#     elif plan=='D':
#         if x==N:
#             continue
#         else:
#             x+=1
#     elif plan=='L':
#         if y==1:
#             continue
#         else:
#             y-=1
#     elif plan=='R':
#         if y==N:
#             continue
#         else:
#             y+=1
#
# print(x, y)


#답지 풀이

n = int(input())
x ,y = 1, 1
plans = input().split()


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y = nx, ny

print(x, y)