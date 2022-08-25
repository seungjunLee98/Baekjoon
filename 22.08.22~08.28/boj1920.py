import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
m = int(input().rstrip())
target_arr = list(map(int, input().split()))
arr.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in range(m):
    print(binary_search(arr, target_arr[i], 0, n-1))


