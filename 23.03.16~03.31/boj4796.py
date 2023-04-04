l, p, v = 1, 1, 1
cnt = 0
while True:
    l, p, v = map(int, input().split())
    if l==0 and p==0 and v==0:
        break
    cnt+=1
    ans = (v//p)*l
    if v%p < l:
        ans += v%p
    else:
        ans += l
    print(f"Case {cnt}: {ans}")