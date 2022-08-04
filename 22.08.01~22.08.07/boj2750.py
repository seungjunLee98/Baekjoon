import sys
n = int(input())
number_list = []

for _ in range(n):
    number = int(sys.stdin.readline())
    number_list.append(number)

number_list.sort()

for i in range(n):
    print(number_list[i])