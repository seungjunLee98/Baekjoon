# def trans(n):
#     if type(n) == int:
#         return int(n)
#     else:
#         return n
#
# n = int(input())
# li = []
# for _ in range(n):
#     li.append(list(map(trans, input().split())))
#
# result = sorted(li, key=lambda x: x[0])
#
# for i in range(len(result)):
#     print(f"{result[i][0]} {result[i][1]}")

import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(member[i][0], member[i][1])
