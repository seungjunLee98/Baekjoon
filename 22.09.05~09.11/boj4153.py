while True:
    leng = list(map(int, input().split()))
    leng.sort()
    if leng[0]==0 and leng[1]==0 and leng[2]==0:
        break
    elif (leng[0]**2 + leng[1]**2) == leng[2]**2:
        print("right")
    else:
        print("wrong")