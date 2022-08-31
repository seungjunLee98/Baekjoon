import sys
input = sys.stdin.readline
n = int(input().rstrip())
li = list(map(int, input().split()))
li.sort()
max_num = int(input().rstrip())
start = 0
end = li[-1]

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        tmp_li = arr[:]
        mid = (start+end)//2
        for i in range(len(tmp_li)):
            if tmp_li[i] > mid:
                tmp_li[i] = mid
        if sum(tmp_li) == target:
            return mid
        elif sum(tmp_li) > target:
            end = mid - 1
        else:
            start = mid + 1
            result = mid

    return result


if sum(li) <= max_num:
    print(li[-1])
else:
    print(binary_search(li, max_num, start, end))



