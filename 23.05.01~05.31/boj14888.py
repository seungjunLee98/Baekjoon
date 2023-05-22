import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
oper_table = list(map(int, input().split())) # +, -, *, //

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:
        dfs(depth+1, total + num_list[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - num_list[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * num_list[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / num_list[depth]), plus, minus, multiply, divide-1)

dfs(1, num_list[0], oper_table[0], oper_table[1], oper_table[2], oper_table[3])
print(maximum)
print(minimum)