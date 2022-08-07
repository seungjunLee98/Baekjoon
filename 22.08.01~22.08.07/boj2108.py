import sys
from collections import Counter


def mean(list):
    mean = round(sum(list)/len(list))
    return mean

def median(list):
    list = sorted(list)
    median = list[(len(list)-1)//2]
    return median

def mode(list):
    list = sorted(list)
    cnt_list = Counter(list).most_common()
    if len(cnt_list) > 1 and cnt_list[0][1] == cnt_list[1][1]:
        return cnt_list[1][0]
    else:
        return cnt_list[0][0]

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

print(mean(num_list))
print(median(num_list))
print(mode(num_list))
print(max(num_list)-min(num_list))