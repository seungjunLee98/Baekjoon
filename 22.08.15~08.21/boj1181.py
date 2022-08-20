
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr = set(arr)
result = sorted(arr)
result = sorted(result, key=len)

print('\n'.join(result))