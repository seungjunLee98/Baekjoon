import sys
input = sys.stdin.readline

k, n = map(int, input().split())
k_li = []
for _ in range(k):
    k_li.append(int(input().rstrip()))

end = max(k_li)

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        cnt = 0
        mid = (start+end)//2
        if mid == 0:
            mid += 1
        for x in arr:
            if x >= mid:
                cnt += x//mid
        if cnt < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return print(result)

binary_search(k_li, n, 0, end)


