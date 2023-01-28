n = int(input())

coin = [500,100,50,10,5,1]

change = 1000-n

result = 0

for i in coin:
    result += change//i
    change = change%i

print(result)