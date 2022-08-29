import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x_li = []
for _ in range(n):
    x_li.append(int(input().rstrip()))

x_li.sort()

def binary_search(arr, start, end):
    while start <= end:
        mid = (start+end)//2
        current = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = x_li[-1] - x_li[0]
answer = 0

binary_search(x_li, start, end)
print(answer)










