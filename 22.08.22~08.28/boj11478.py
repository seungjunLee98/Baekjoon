s = input()
res = set()
size_s = len(s)
for i in range(size_s):
    for j in range(i, size_s):
        res.add(s[i:j+1])

print(len(res))
