# def merge_sort(arr):
#     def sort(low, high):
#         if high - low < 2:
#             return
#         mid = (low + high) // 2
#         sort(low, mid)
#         sort(mid, high)
#         merge(low, mid, high)
#
#     def merge(low, mid, high):
#         temp = []
#         l, h = low, mid
#         global ans
#
#         while l < mid and h < high:
#             if arr[l] < arr[h]:
#                 temp.append(arr[l])
#                 ans.append(arr[l])
#                 l += 1
#             else:
#                 temp.append(arr[h])
#                 ans.append(arr[h])
#                 h += 1
#
#         while l < mid:
#             temp.append(arr[l])
#             ans.append(arr[l])
#             l += 1
#         while h < high:
#             temp.append(arr[h])
#             ans.append(arr[h])
#             h += 1
#
#         for i in range(low, high):
#             arr[i] = temp[i - low]
#     return sort(0, len(arr))
#
# size_A, k = map(int,input().split())
# ans = []
# array_A = list(map(int, input().split()))
# merge_sort(array_A)
#
# if len(ans) < k:
#     print(-1)
# else:
#     print(ans[k-1])

import sys

input = sys.stdin.readline


def mergeSort(L):
    if len(L) == 1:
        return L

    mid = (len(L) + 1) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])

    L2 = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j += 1

    return L2


n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
mergeSort(a)

if len(ans) >= k:
    print(ans[k - 1])
else:
    print(-1)
