import sys
input = sys.stdin.readline

n = int(input())
my_card = list(map(int, input().split()))
m = int(input())
check_card = list(map(int, input().split()))

my_card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(my_card, check_card[i], 0, n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')

import sys

def test():
    input()
    b = set(input().split()) #내가 가진 값
    input()
    d = input().split()    #찾아야 하는 값
    res = ''
    for i in d:
        if i in b:
            res += '1 '
        else:
            res += '0 '
    print(res)

test()
