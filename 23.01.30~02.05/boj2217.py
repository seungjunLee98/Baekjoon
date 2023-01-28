import sys

input = sys.stdin.readline

n = int(input())
rope = []
max_value = 0

for i in range(n):
    rope.append(int(input()))

rope.sort()

for i in range(len(rope)):
    max_value = max(rope[i]*(len(rope)-i), max_value)

print(max_value)