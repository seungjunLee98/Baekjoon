# n = int(input())
# cnt_li = [0 for _ in range(n)]
# li = list(map(int, input().split()))
#
# sor_li = sorted(li)
#
# for i in range(n):
#     for j in range(n):
#         if li[i] == sor_li[j]:
#             cnt_li[i] = len(sor_li[:j])
#             break
#
# for k in cnt_li:
#     print(k, end=' ')
import sys
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
sor_li = list(sorted(set(li)))

dic = {sor_li[i]: i for i in range(len(sor_li))}

for i in li:
  print(dic[i],end=' ')
