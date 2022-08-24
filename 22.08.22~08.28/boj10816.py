# from collections import Counter
# import sys
# input = sys.stdin.readline
#
# n = int(input().rstrip())
# card = list(map(int, input().split()))
# m = int(input().rstrip())
# test = list(map(int, input().split()))
#
# count = Counter(card)
#
# for i in range(m):
#     if test[i] in count:
#         print(count[test[i]], end=' ')
#     else:
#         print(0, end=' ')

import sys
input = sys.stdin.readline

n = int(input().rstrip())
card = list(map(int, input().split()))
m = int(input().rstrip())
test = list(map(int, input().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')